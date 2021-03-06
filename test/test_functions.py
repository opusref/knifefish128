# 
# Copyright (c) 2018-2019, Michael Harper
# 
# See LICENSE for licensing information

#!/usr/bin/python3

import subprocess

tests = {
    "pht"   :"pht/test_pht",
    "sbox" : "sbox/test_sbox",
    "pbox" : "pbox/test_pbox",
    "expand_passphrase" : "expand_passphrase/test_expand_passphrase",
    "invert_ctx" : "invert_ctx/test_invert_ctx",
    "block" :"block/test_block",
    "encrypt_file_cbc" : "encrypt_file_cbc/test_encrypt_file_cbc",
    }

exit_codes = {}

print("\n[*] Running tests.\n")

for k in tests.keys():

    child = subprocess.Popen("test/" + tests[k], stdout=subprocess.PIPE)
    data = child.communicate()[0]
    code = child.returncode

    exit_codes[k] = code

    print (data.decode("ascii"),end='')

all_passed = True

for k in exit_codes.keys():

    if exit_codes[k] > 0:

        print(str(exit_codes[k]) + " tests failed in " + k + "\n")

        all_passed = False

if all_passed:
        print("[*] All tests passed.\n")


