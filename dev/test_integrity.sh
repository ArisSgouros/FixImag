#!/bin/bash

# Beware! Set it to true only if you know what you know what you are doing!
inspect_log=true
replace_log=false

difftool="vimdiff"
#difftool="diff"

echo
if [ "$replace_log" = true ] ; then
   echo -e "Flag replace_log is set to true. You will have the option to \e[32mREPLACE\e[0m log files."
fi

examplesPath="$(pwd)"
echo "Path of Examples: $examplesPath"

declare -a EXAMPLES=( \
   "$examplesPath/test_deform/" \
   "$examplesPath/test_imag_box/" \
   "$examplesPath/test_imag_strain/" \
)

: '
# Start of comments section
# End of comments section
'

echo 'Initiating tests..'
echo '-----------------------------------------------------------------'

for modulePath in "${EXAMPLES[@]}"; do
   echo
   echo "Testing example: $modulePath"

   cd "$modulePath"

   ./clean.sh

   echo "Running the test.."
   python run.py > 0.log

   mapfile -t LOG_LIST < "$modulePath/LOG_LIST"

   for LOG in "${LOG_LIST[@]}"; do

      if [[ $LOG == "#"* ]]; then continue; fi

      new_log="$LOG"
      ref_log="REF/$new_log"

      if ! test -f "$new_log"; then
         echo -e "LOG FILE: \e[36m$new_log\e[0m .. \e[93mNOT FOUND!\e[0m"
         continue
      fi
      if ! test -f "$ref_log"; then
         echo -e "REF LOG FILE: \e[36m$ref_log\e[0m .. \e[93mNOT FOUND!\e[0m"
         if [ "$replace_log" = true ] ; then
            read -p "Do you want to RESTORE the missing log? (Y/n)" -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
               cp "$new_log" "$ref_log"
            fi
         fi
         continue
      fi

      OUTPUT="$(diff -q "$new_log" "$ref_log")"

      if [ -z "$OUTPUT" ]
      then
         echo -e "LOG FILE: \e[36m$new_log\e[0m .. \e[32mSUCCESS!\e[0m"
      else
         if [ "$say_fail" = true ] ; then
           spd-say fail
         fi
         echo -e "LOG FILE: \e[36m$new_log\e[0m .. \e[31mFAILED!\e[0m"
         echo "${OUTPUT}"

         if [ "$inspect_log" = true ] ; then
            read -p "Do you want to inspect the mismatched logs? (Y/n)" -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
               "$difftool" "$new_log" "$ref_log"
            fi
         fi
         if [ "$replace_log" = true ] ; then
            read -p "Do you want to REPLACE the mismatched logs? (Y/n)" -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
               cp "$new_log" "$ref_log"
            fi
         fi
      fi
   done
   cd "$examplesPath"
done
