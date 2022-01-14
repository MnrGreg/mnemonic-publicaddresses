## crypto public address -> mnemonic phrase
- exploring possibilities to derive mnemonic phrases from 40bit public addresses
- optimal solution would be 3-4 color-coded adjective/nouns:
<span style="color:red">jumping.cardinals</span>
<span style="color:yellow">excited.rangers</span>
<span style="color:blue">wild.safaris</span>

### approach:
- bitcoin bip-0039 wordlist * 10 colors * 900 adjectives = wordlist of 17mil = 7x color/adjective/noun combinations 
- adoption would require industry standard to be formed
- systematic determination seems very CPU expensive
- checksum still needed

### use-cases:
- payments to parties where proximity to QR codes is not possible (e.g. voice calls)
- for the unbanked that are less able to afford ENS
- etherscan, etc would be much easier to read