import requests
import requests_cache
import base64
import bs4
import os

requests_cache.install_cache('demo_cache')

MUFI = {
    (224, 4): 'A',
    (224, 10): 'A',
    (224, 16): 'A',
    (224, 37): 'A',
    (224, 44): 'ae',
    (224, 51): 'A',
    (224, 54): 'AE',
    (224, 58): 'AE',
    (224, 61): 'AE',
    (224, 63): 'AE',
    (224, 64): 'AE',
    (224, 65): 'AE',
    (224, 66): 'AE',
    (224, 67): 'AE',
    (224, 68): 'B',
    (224, 102): 'C',
    (224, 118): 'C',
    (224, 119): 'D',
    (224, 143): 'ETH',
    (224, 153): 'E',
    (224, 183): 'E',
    (224, 188): 'E',
    (224, 200): 'E',
    (224, 209): 'E',
    (224, 225): 'ea',
    (224, 232): 'E',
    (224, 233): 'E',
    (224, 234): 'E',
    (224, 235): 'E',
    (224, 236): 'E',
    (224, 238): 'F',
    (224, 240): 'F',
    (225, 1): 'G',
    (225, 22): 'H',
    (225, 42): 'I',
    (225, 53): 'I',
    (225, 55): 'I',
    (225, 67): 'I',
    (225, 80): 'I',
    (225, 81): 'J',
    (225, 82): 'J',
    (225, 83): 'J',
    (225, 84): 'J',
    (225, 92): 'J',
    (225, 98): 'J',
    (225, 99): 'J',
    (225, 104): 'K',
    (225, 158): 'L',
    (225, 184): 'M',
    (225, 210): 'M',
    (225, 220): 'N',
    (226, 8): 'O',
    (226, 12): 'O',
    (226, 27): 'O',
    (226, 45): 'O',
    (226, 68): 'oe',
    (226, 70): 'ou',
    (226, 79): 'O',
    (226, 82): 'O',
    (226, 83): 'O',
    (226, 85): 'O',
    (226, 87): 'O',
    (226, 89): 'OE',
    (226, 93): 'OE',
    (226, 96): 'OE',
    (226, 98): 'OE',
    (226, 104): 'P',
    (226, 109): 'P',
    (226, 130): 'Q',
    (226, 136): 'Q',
    (226, 226): 'T',
    (226, 238): 'T',
    (227, 9): 'U',
    (227, 11): 'U',
    (227, 21): 'U',
    (227, 23): 'U',
    (227, 36): 'U',
    (227, 43): 'ue',
    (227, 45): 'uo',
    (227, 49): 'U',
    (227, 55): 'TH',
    (227, 58): 'V',
    (227, 59): 'V',
    (227, 66): 'V',
    (227, 75): 'V',
    (227, 76): 'V',
    (227, 77): 'V',
    (227, 78): 'V',
    (227, 80): 'W',
    (227, 83): 'we',
    (227, 87): 'W',
    (227, 115): 'Y',
    (227, 117): 'Y',
    (227, 118): 'Y',
    (227, 124): 'Y',
    (227, 132): 'Y',
    (227, 133): 'Y',
    (227, 159): 'TH',
    (227, 211): 'O',
    (227, 212): 'O',
    (227, 229): 'F',
    (227, 230): 'V',
    (227, 231): 'V',
    (228, 4): 'a',
    (228, 10): 'a',
    (228, 16): 'a',
    (228, 26): 'a',
    (228, 29): 'a',
    (228, 31): 'a',
    (228, 37): 'a',
    (228, 44): 'ae',
    (228, 45): 'ao',
    (228, 46): 'av',
    (228, 51): 'a',
    (228, 54): 'ae',
    (228, 58): 'ae',
    (228, 61): 'ae',
    (228, 63): 'ae',
    (228, 64): 'ae',
    (228, 65): 'ae',
    (228, 66): 'ae',
    (228, 67): 'ae',
    (228, 68): 'b',
    (228, 77): 'b',
    (228, 102): 'c',
    (228, 118): 'c',
    (228, 119): 'd',
    (228, 143): 'eth',
    (228, 145): 'd',
    (228, 152): 'e',
    (228, 153): 'e',
    (228, 159): 'e',
    (228, 183): 'e',
    (228, 188): 'e',
    (228, 200): 'e',
    (228, 205): 'e',
    (228, 207): 'e',
    (228, 209): 'e',
    (228, 225): 'ea',
    (228, 226): 'ei',
    (228, 227): 'ev',
    (228, 232): 'e',
    (228, 233): 'e',
    (228, 234): 'e',
    (228, 235): 'e',
    (228, 236): 'e',
    (228, 238): 'f',
    (228, 240): 'f',
    (229, 1): 'g',
    (229, 22): 'h',
    (229, 23): 'h',
    (229, 42): 'i',
    (229, 53): 'i',
    (229, 55): 'i',
    (229, 67): 'i',
    (229, 72): 'i',
    (229, 74): 'ie',
    (229, 75): 'iv',
    (229, 80): 'i',
    (229, 81): 'j',
    (229, 82): 'j',
    (229, 83): 'j',
    (229, 84): 'j',
    (229, 98): 'j',
    (229, 99): 'j',
    (229, 104): 'k',
    (229, 140): 'l',
    (229, 150): 'l',
    (229, 158): 'l',
    (229, 164): 'l',
    (229, 177): 'l',
    (229, 184): 'm',
    (229, 197): 'm',
    (229, 210): 'm',
    (229, 215): 'n',
    (229, 220): 'n',
    (229, 238): 'n',
    (230, 8): 'o',
    (230, 12): 'o',
    (230, 14): 'o',
    (230, 27): 'o',
    (230, 44): 'o',
    (230, 45): 'o',
    (230, 55): 'o',
    (230, 67): 'oa',
    (230, 68): 'oe',
    (230, 69): 'oi',
    (230, 70): 'ou',
    (230, 71): 'ov',
    (230, 79): 'o',
    (230, 82): 'o',
    (230, 83): 'o',
    (230, 85): 'o',
    (230, 87): 'o',
    (230, 89): 'oe',
    (230, 93): 'oe',
    (230, 96): 'oe',
    (230, 98): 'oe',
    (230, 101): 'p',
    (230, 104): 'p',
    (230, 109): 'p',
    (230, 129): 'q',
    (230, 130): 'q',
    (230, 136): 'q',
    (230, 139): 'q',
    (230, 163): 'r',
    (230, 226): 't',
    (230, 238): 't',
    (231, 9): 'u',
    (231, 11): 'u',
    (231, 21): 'u',
    (231, 23): 'u',
    (231, 36): 'u',
    (231, 39): 'u',
    (231, 43): 'ue',
    (231, 44): 'ui',
    (231, 45): 'uo',
    (231, 49): 'u',
    (231, 52): 'ths',
    (231, 53): 'ths',
    (231, 55): 'th',
    (231, 58): 'v',
    (231, 59): 'v',
    (231, 66): 'v',
    (231, 67): 'v',
    (231, 75): 'v',
    (231, 76): 'v',
    (231, 77): 'v',
    (231, 78): 'v',
    (231, 79): 'v',
    (231, 80): 'w',
    (231, 83): 'we',
    (231, 84): 'wo',
    (231, 87): 'w',
    (231, 115): 'y',
    (231, 117): 'y',
    (231, 118): 'y',
    (231, 123): 'y',
    (231, 124): 'y',
    (231, 129): 'ye',
    (231, 132): 'y',
    (231, 133): 'y',
    (231, 158): 's',
    (231, 159): 'th',
    (231, 162): 'th',
    (231, 178): 'n',
    (231, 193): 'r',
    (231, 194): 's',
    (231, 195): 'k',
    (231, 199): 'hs',
    (231, 200): 'ks',
    (231, 204): 'o',
    (231, 211): 'o',
    (231, 212): 'o',
    (231, 228): 'r',
    (231, 229): 'f',
    (231, 230): 'v',
    (231, 231): 'v',
    (232, 161): 'i',
    (232, 162): 'j',
    (232, 163): 'AUTEM',
    (232, 179): 'qr',
    (232, 180): 'q',
    (232, 183): 's',
    (232, 184): 's',
    (232, 186): 'v',
    (232, 187): 'v',
    (232, 188): 'v',
    (232, 189): 'x',
    (232, 190): 'x',
    (232, 191): 'qet',
    (232, 193): 'thr',
    (232, 194): 'hr',
    (232, 195): 'hr',
    (232, 197): 'kr',
    (232, 198): 'UU',
    (232, 199): 'uu',
    (232, 200): 'UE',
    (232, 201): 'ue',
    (232, 206): 'x',
    (232, 209): 'ae',
    (232, 211): 'ae',
    (232, 213): 'a',
    (232, 215): 'o',
    (232, 221): 'i',
    (232, 222): 'or',
    (232, 223): 'sl',
    (232, 224): 'ai',
    (232, 225): 'au',
    (232, 226): 'ee',
    (232, 227): 'eo',
    (232, 228): 'ia',
    (232, 229): 'io',
    (232, 230): 'iu',
    (232, 231): 'je',
    (232, 232): 'me',
    (232, 233): 'oo',
    (232, 234): 're',
    (232, 235): 'ua',
    (232, 236): 'uv',
    (232, 237): 'uw',
    (232, 240): 'wa',
    (232, 241): 'wi',
    (232, 242): 'wu',
    (232, 243): 'wv',
    (234, 208): 'gr',
    (234, 209): 'qv',
    (234, 210): 'gp',
    (234, 218): 'st',
    (234, 240): 'a',
    (234, 241): 'ae',
    (234, 242): 'ao',
    (234, 243): 'e',
    (235, 160): 'sa',
    (235, 161): 'sh',
    (235, 162): 'si',
    (235, 163): 'sl',
    (235, 164): 'so',
    (235, 165): 'sp',
    (235, 166): 'ss',
    (235, 167): 'ssi',
    (235, 168): 'ssl',
    (235, 169): 'sti',
    (235, 170): 'str',
    (235, 171): 'su',
    (235, 172): 'sv',
    (235, 173): 'hs',
    (235, 174): 'ks',
    (235, 175): 's',
    (235, 176): 'AV',
    (235, 177): 'av',
    (235, 178): 'd',
    (235, 179): 'F',
    (235, 180): 'f',
    (235, 181): 'M',
    (235, 182): 'm',
    (235, 183): 'O',
    (235, 184): 'o',
    (235, 185): 'r',
    (235, 186): 'V',
    (235, 187): 'v',
    (235, 189): 'ea',
    (235, 190): 'eu',
    (235, 191): 'uy',
    (235, 192): 'AO',
    (235, 193): 'ao',
    (235, 194): 'AV',
    (235, 195): 'av',
    (235, 196): 'O',
    (235, 197): 'o',
    (235, 198): 'O',
    (235, 199): 'o',
    (235, 200): 'OE',
    (235, 201): 'oe',
    (235, 202): 'YY',
    (235, 203): 'yy',
    (235, 205): 'O',
    (235, 206): 'o',
    (235, 207): 'P',
    (235, 208): 'B',
    (235, 209): 'd',
    (235, 210): 'D',
    (235, 211): 'F',
    (235, 212): 'f',
    (235, 213): 'f',
    (235, 214): 'f',
    (235, 215): 'F',
    (235, 218): 'H',
    (235, 219): 'K',
    (235, 220): 'L',
    (235, 221): 'M',
    (235, 222): 'O',
    (235, 223): 'o',
    (235, 224): 'O',
    (235, 225): 'o',
    (235, 226): 'J',
    (235, 227): 'j',
    (235, 228): 'OO',
    (235, 229): 'oo',
    (235, 230): 'PP',
    (235, 231): 'pp',
    (235, 232): 'YY',
    (235, 233): 'yy',
    (235, 234): 'AE',
    (235, 235): 'ae',
    (235, 236): 'O',
    (235, 237): 'o',
    (235, 238): 'O',
    (235, 239): 'o',
    (235, 240): 'AV',
    (235, 241): 'av',
    (235, 242): 'E',
    (235, 243): 'e',
    (235, 244): 'A',
    (235, 245): 'a',
    (235, 246): 'I',
    (235, 247): 'i',
    (235, 248): 'O',
    (235, 249): 'o',
    (235, 250): 'O',
    (235, 251): 'o',
    (235, 252): 'O',
    (235, 253): 'o',
    (235, 254): 'U',
    (235, 255): 'u',
    (238, 194): 'bb',
    (238, 195): 'bg',
    (238, 196): 'ck',
    (238, 197): 'ct',
    (238, 198): 'dd',
    (238, 199): 'ey',
    (238, 200): 'fa',
    (238, 201): 'fj',
    (238, 202): 'fr',
    (238, 203): 'ft',
    (238, 204): 'fu',
    (238, 205): 'fy',
    (238, 206): 'fft',
    (238, 207): 'ffy',
    (238, 208): 'fty',
    (238, 209): 'gg',
    (238, 210): 'gd',
    (238, 211): 'gd',
    (238, 212): 'geth',
    (238, 213): 'ns',
    (238, 214): 'pp',
    (238, 215): 'pp',
    (238, 216): 'tr',
    (238, 217): 'tt',
    (238, 218): 'tt',
    (238, 219): 'ty',
    (238, 220): 'tz',
    (238, 221): 'PP',
    (238, 222): 'go',
    (238, 223): 's',
    (238, 224): 'a',
    (238, 225): 'b',
    (238, 226): 'c',
    (238, 227): 'd',
    (238, 228): 'd',
    (238, 229): 'eth',
    (238, 230): 'e',
    (238, 231): 'f',
    (238, 232): 'g',
    (238, 233): 'h',
    (238, 234): 'i',
    (238, 235): 'j',
    (238, 236): 'k',
    (238, 237): 'l',
    (238, 238): 'm',
    (238, 239): 'n',
    (238, 240): 'o',
    (238, 241): 'p',
    (238, 242): 'q',
    (238, 243): 'r',
    (238, 244): 's',
    (238, 245): 't',
    (238, 246): 'th',
    (238, 247): 'u',
    (238, 248): 'v',
    (238, 249): 'w',
    (238, 250): 'x',
    (238, 251): 'y',
    (238, 252): 'z',
    (238, 253): 'i',
    (238, 254): 'j',
    (238, 255): 'f',
    (239, 12): 'Q',
    (239, 17): 'X',
    (239, 21): 'TH',
    (239, 32): 'G',
    (239, 33): 'N',
    (239, 34): 'R',
    (239, 35): 'S',
    (239, 36): 'T',
    (239, 37): 'B',
    (239, 38): 'D',
    (239, 39): 'G',
    (239, 40): 'L',
    (239, 41): 'M',
    (239, 42): 'N',
    (239, 43): 'R',
    (239, 44): 'S',
    (239, 45): 'T',
    (239, 160): 'aa',
    (239, 161): 'ae',
    (239, 162): 'av',
    (239, 163): 'af',
    (239, 164): 'af',
    (239, 165): 'ag',
    (239, 166): 'al',
    (239, 167): 'an',
    (239, 168): 'an',
    (239, 169): 'ap',
    (239, 170): 'ar',
    (239, 171): 'ar',
    (239, 172): 'ath',
    (239, 173): 'oc',
    (239, 174): 'AE',
    (239, 216): 'uu',
    (239, 217): 'UU',
    (239, 219): 'AE',
    (239, 220): 'ae',
    (239, 221): 'oe',
    (239, 222): 'ao',
    (239, 223): 'aa',
    (239, 224): 'AA',
    (239, 225): 'aa',
    (239, 226): 'AO',
    (239, 227): 'ao',
    (239, 228): 'AU',
    (239, 229): 'au',
    (239, 230): 'AV',
    (239, 231): 'av',
    (239, 232): 'OO',
    (239, 233): 'oo',
    (239, 234): 'AA',
    (239, 235): 'aa',
    (239, 236): 'OO',
    (239, 237): 'oo',
    (239, 238): 'AA',
    (239, 239): 'aa',
    (239, 240): 'AY',
    (239, 241): 'ay',
    (239, 242): 'AA',
    (239, 243): 'aa',
    (239, 244): 'AO',
    (239, 245): 'ao',
    (239, 246): 'AU',
    (239, 247): 'au',
    (239, 248): 'AV',
    (239, 249): 'av',
    (239, 250): 'AY',
    (239, 251): 'ay',
    (239, 252): 'OO',
    (239, 253): 'oo',
    (239, 254): 'AA',
    (239, 255): 'aa',
    (240, 10): '_',
    (240, 11): '_',
    (240, 12): '_',
    (240, 13): '_',
    (240, 18): 'b',
    (240, 19): 'B',
    (240, 22): 'D',
    (240, 23): 'f',
    (240, 28): 'K',
    (240, 37): 'p',
    (240, 42): 'T',
    (240, 43): 'y',
    (240, 47): 'i',
    (240, 48): 'j',
    (240, 49): 'j',
    (240, 50): 'o',
    (240, 51): 'q',
    (240, 54): 'an',
    (240, 56): 'ar',
    (240, 58): 'an',
    (240, 59): 'T',
    (240, 60): 'w',
    (240, 61): 'th',
    (240, 62): 'or',
    (240, 63): 'orum',
    (240, 64): 'rum',
    (241, 6): 'C',
    (241, 10): 'E',
    (241, 14): 'G',
    (241, 16): 'H',
    (241, 26): 'M',
    (241, 38): 'S',
    (241, 39): 's',
    (241, 40): 's',
    (241, 48): 'ar',
    (241, 53): 'e',
    (241, 54): 'e',
    (241, 58): 'A',
    (241, 62): 'o',
    (241, 63): 'o',
    (241, 66): 'ET',
    (241, 73): 'th',
    (241, 83): '_',
    (241, 88): 'et',
    (241, 89): 'de',
    (241, 96): '!',
    (241, 97): ';',
    (241, 147): 'd',
    (241, 148): 'f',
    (241, 149): 'k',
    (241, 150): 'g',
    (241, 152): 'c',
    (241, 153): 't',
    (241, 154): 'n',
    (241, 155): 'r',
    (241, 165): 'US',
    (241, 166): 'us',
    (241, 167): 'ET',
    (241, 172): ';',
    (241, 187): 'ch',
    (241, 188): 'fo',
    (241, 189): '0',
    (241, 191): 'X',
    (241, 192): '_',
    (241, 193): 'RAA',
    (241, 194): 'ur',
    (241, 197): '_',
    (241, 199): '_',
    (241, 200): '_',
    (241, 202): '_',
    (241, 204): '_',
    (241, 210): '_',
    (241, 218): '_',
    (241, 224): ',',
    (241, 225): '_',
    (241, 226): ',',
    (241, 227): ',',
    (241, 228): '.',
    (241, 229): ';',
    (241, 230): ',',
    (241, 231): '!',
    (241, 232): '!',
    (241, 234): ';',
    (241, 236): '_',
    (241, 240): ';',
    (241, 241): '!',
    (241, 242): ',',
    (241, 244): ',',
    (241, 245): '.',
    (241, 247): ',',
    (241, 248): '/',
    (241, 249): '_',
    (241, 250): ';',
    (241, 251): ';',
    (241, 252): '_',
    (242, 0): 'a',
    (242, 1): 'A',
    (242, 2): 'a',
    (242, 3): 'a',
    (242, 4): 'ae',
    (242, 5): 'AO',
    (242, 6): 'ao',
    (242, 7): 'f',
    (242, 8): 'k',
    (242, 9): 'k',
    (242, 20): 'a',
    (242, 21): 'a',
    (242, 23): 'E',
    (242, 24): 'e',
    (242, 25): 'e',
    (242, 26): 'e',
    (242, 27): 'f',
    (242, 28): 'f',
    (242, 29): 'g',
    (242, 30): 'g',
    (242, 31): 'g',
    (242, 32): 'i',
    (242, 33): 'k',
    (242, 34): 'l',
    (242, 35): 'm',
    (242, 36): 'M',
    (242, 37): 'm',
    (242, 38): 'm',
    (242, 40): 'n',
    (242, 41): 'N',
    (242, 42): 'N',
    (242, 43): 'N',
    (242, 44): 'Q',
    (242, 51): 'y',
    (242, 58): 'h',
    (242, 60): 'm',
    (242, 61): 'm',
    (242, 62): 'm',
    (242, 63): 'C',
    (242, 224): '_',
    (242, 226): 'X',
    (242, 227): 'Y',
    (242, 228): 'D',
    (242, 230): '_',
    (242, 231): '_',
    (242, 232): 'F',
    (242, 233): '_',
    (242, 234): '£',
    (242, 235): '£',
    (242, 236): '£',
    (242, 237): '£',
    (242, 238): '_',
    (242, 239): '_',
    (242, 240): 'm',
    (242, 241): 'm',
    (242, 242): 'm',
    (242, 243): 'f',
    (242, 244): '_',
    (242, 245): '_',
    (242, 246): '_',
    (242, 247): '_',
    (242, 248): '_',
    (242, 249): '_',
    (242, 250): '_',
    (242, 251): '_',
    (242, 253): '_',
    (242, 254): 'C',
    (242, 255): 'c',
    (244, 249): 'll',
    (244, 250): 'sch',
    (244, 251): 'sj',
    (244, 252): 'sk',
    (244, 253): 'ss',
    (244, 254): 'ssk',
    (244, 255): 'sst',
    (247, 4): 'm',
    (247, 5): 'm',
    (247, 6): 'm',
    (247, 7): 'm',
    (247, 8): 'm',
    (247, 9): 'm',
    (247, 11): 'm',
    (247, 12): 'm',
    (247, 21): 'm',
    (247, 22): 'm',
    (247, 23): 'm',
    (247, 24): 'm',
    (247, 25): 'm',
    (247, 26): 'm',
    (247, 27): 'm',
    (247, 28): 'm',
    (247, 178): 'V',
    (247, 179): 'X',
    (247, 180): 'L',
    (247, 181): 'C',
    (247, 182): 'D'
}
MUFI[(32, 74)] = "et"
MUFI[(167, 110)] = MUFI[(167, 111)] = "us"


def get_base64_image(url):
    response = requests.get("https://skaldic.abdn.ac.uk/"+ url)
    uri = ("data:" +
           response.headers['Content-Type'] + ";" +
           "base64," + base64.b64encode(response.content).decode("utf-8"))
    return uri


base_uri = "https://skaldic.abdn.ac.uk/m.php?p=mufichars&i=1&v="

ignore_code = ["- spacing", "- symbols", "- punctuation", "- numbers", "- combining"]

for char in [
    "A", "B", "C", "D", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z"
] + ignore_code:
    data = requests.get(base_uri+char)
    data.raise_for_status()
    with open(os.path.join(os.path.dirname(__file__), char.replace("- ", "")+".html"), "w") as f:
        f.write("""<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>""" + char + """ transcription file</title>

</head>

<body>
<table border="1">
    <thead><tr><th>Image</th><th>Transcription</th><th>Description</th><th>Code</th></thead>
    <tbody>
    """)
        doc = bs4.BeautifulSoup(data.text, features="html.parser")
        for element in doc.select("ul[data-split-icon='edit'] li"):
            desc = element.select_one("p").text
            code = element.select_one("h2").text
            image = get_base64_image(element.select_one("img").attrs["src"])

            transc = char if char not in ignore_code else ""

            if "SMALL" in desc:
                transc = transc.lower()

            c = int(code, 16)
            section, position = c >> 8, c % 256
            transc = MUFI.get((section, position), transc)

            f.write("""<tr><td><img src="{base64}" height="20"/></td><td contenteditable="true">{char}</td><td>{desc}</td><td>{code}</td></tr>\n""".format(
                base64=image,
                code=code,
                char=transc,
                desc=desc
            ))
        f.write("""
        </tbody></table></body>
    </html>""")