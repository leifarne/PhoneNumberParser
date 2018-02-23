import PhoneNumber as PN
import sys

try:
    if len(sys.argv) < 3:
        raise TypeError("Not enough input arguments")
    elif len(sys.argv) > 3:
        raise TypeError("Too many input arguments")
except TypeError as err:
    print err
    
  #TODO: Her er det en strukturfeil. Programmet må termineres etter exception, ellers fortsetter det bare på neste linje.

in_file = sys.argv[1]
out_file = sys.argv[2]

line_number = 0
raw_number = ""  # Unnormalized

#TODO: Bruk klassetyper. Jeg skal sjekke hvordan det gjøres.
phone_number = {"45": PN.DanishPhoneNumber(),
                "46": PN.SwedishPhoneNumber(),
                "47": PN.NorwegianPhoneNumber()}
input_file = open(in_file, "r")
output_file = open(out_file, "w")

# With statement is exited early when using exceptions
while True:
    raw_number = input_file.readline()

    # End of input_file
    if not raw_number:
        input_file.close()
        output_file.close()
        break

    try:
        number = PN.PhoneNumber.normalize(raw_number)
        #TODO: Her bør objektet instansieres - på bakgrunn av landkode. Og etterfølgende kode jobber på den spesifikke nummer-instansen.
        country = PN.PhoneNumber.identify_country(number)
        phone_number[country].parse(number)  # Accepts normalized numbers only

        # No exceptions raised. Number is correct
        number = phone_number[country].format()
        output_file.write(number + "\n")

        line_number += 1

    except TypeError as err:
        #TODO: bruk string interpolation for å formatere ut-strengen.
        msg = "TypeError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
        output_file.write(raw_number)
    except IndexError as err:
        msg = "IndexError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
    except ValueError as err:
        msg = "ValueError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
        output_file.write(raw_number)
