import operator


cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""


class Attack:

    def __init__(self):
        self.cipher = cipher
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.plain_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.freq_english = {
            'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
            'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
            'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
            'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
            'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
            'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
            'y': 0.01974, 'z': 0.00074
        }

        self.freq = {}
        self.mappings = {}
        self.key = {}

    def calculate_freq(self, cipher):
        self.freq = {c : 0 for c in self.alphabet}
        letter_counter = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_counter += 1

        for c in self.freq:
            self.freq[c] = self.freq[c] / letter_counter

    def print_freq(self):
        for c in self.freq:
            print(f"{c} : {round(self.freq[c],4)}")

    def calculate_matches(self):
        """
        map all possible combinations of cipher
        """
        for cipher_char in self.alphabet:
            map = {}
            for plain_char in self.alphabet:
                map[plain_char] = round(abs(self.freq[cipher_char] -  self.freq_english[plain_char]), 4)

            self.mappings[cipher_char] = sorted(map.items(), key=operator.itemgetter(1))

    def guess_key(self):
        for cipher_char in self.cipher_chars_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_chars_left:
                    self.key[cipher_char] = plain_char
                    self.plain_chars_left = self.plain_chars_left.replace(plain_char, "")
                    break
        
    def get_key(self):
        return self.key

    def set_key_mapping(self, cipher_char, plain_char):
        """
        set individual keys we are sure of
        """

        if cipher_char not in self.cipher_chars_left  \
            or plain_char not in self.plain_chars_left:
            print("Error: key mapping error. {cipher_char} -> {plain_char}")
            exit(1)

        self.key[cipher_char] = plain_char
        self.plain_chars_left = self.plain_chars_left.replace(plain_char, "")
        self.cipher_chars_left = self.cipher_chars_left.replace(cipher_char, "")

def decrypt(key, cipher):
    plain = ""
    for c in cipher:
        if c in key:
            plain += key[c]
        else:
            plain += c

    return plain

if __name__ == "__main__":
    a = Attack()
    a.calculate_freq(cipher)
    # a.print_freq()
    a.calculate_matches()
    # print(a.mappings)
    a.set_key_mapping('r', 'e')
    a.set_key_mapping('b', 't')
    a.set_key_mapping('j', 'o')
    a.set_key_mapping('x', 'f')
    a.set_key_mapping('m', 'a')
    a.set_key_mapping('v', 'c')
    a.set_key_mapping('p', 'h')
    a.set_key_mapping('h', 'l')
    a.set_key_mapping('k', 'n')
    a.set_key_mapping('c', 'w')
    a.set_key_mapping('t', 'y')
    a.set_key_mapping('y', 'm')
    a.set_key_mapping('s', 'p')
    a.set_key_mapping('q', 'k')
    a.set_key_mapping('a', 'x')
    a.set_key_mapping('g', 'z')
    a.set_key_mapping('f', 'q')

    a.guess_key()
    key =  a.get_key()

    for k,v in key.items():
        print(f"{k} -> {v}")

    print(decrypt(key, cipher))
    # print(key)