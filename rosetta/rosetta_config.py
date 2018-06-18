class RosettaConfig(object):
    # Keep the list of fields and their english representation.

    FIELDS_LIST = {
        'מספר ני"ע': 'instrument_id',
        'מספר מנפיק': 'issuer_id',
        'דירוג': 'rating',
        'שם מדרג': 'rating_agency',
        'סוג מטבע': 'currency',
        'שיעור ריבית': 'interest_rate',
        'תשואה לפידיון': 'yield',
        'שווי שוק': 'market_cap',
        'שעור מנכסי אפיק ההשקעה': 'rate_of_investment_channel',
        'שעור מסך נכסי השקעה': 'rate_of_fund',
        'זירת מסחר': 'trading_floor',
        'תאריך רכישה': 'date_of_purchase',
        'מח"מ': 'average_of_duration',
        'ערך נקוב': 'par_value',
        'שער': 'rate',
        'שעור מערך נקוב מונפק': 'rate_of_ipo',
        'ספק המידע': 'informer',
        'שווי הוגן': 'fair_value',
        'ענף מסחר': 'activity_industry',
        'תאריך שערוך אחרון': 'date_of_revaluation',
        'אופי הנכס': 'type_of_asset',
        'שעור תשואה במהלך התקופה': 'tmp_name',
        'סכום ההתחייבות': 'liabilities',
        'תאריך סיום ההתחייבות': 'expiry_date_of_liabilities',
        'שער ריבית': 'rate',
        'ריבית אפקטיבית': 'effective_rate',
        'עלות מתואמת': 'coordinated_cost',
        'נכס הבסיס': 'underlying_asset',
        'קונסורציום כן/לא': 'consortium',
        'שיעור ריבית ממוצע': 'average_rate',
        'שווי מוערך': 'par_value',
        'כתובת הנכס': 'instrument_address',
        'פדיון/ ריבית לקבל': 'revenue_interest_receivable',
        'שם המנפיק/שם נייר ערך': 'issuer_name',
        'תנאי ושיעור ריבית': 'condition_and_interest_rate',
        'agencyplusrating': 'agencyplusrating',
    }

    # Hold the list of the sheets and their code.
    INSTRUMENT_DICT = {
        'מזומנים': 'cash',
        'תעודות התחייבות ממשלתיות': 'gdc',
        'תעודות חוב מסחריות': 'cdc',
        'אג"ח קונצרני': 'cb',
        'מניות': 'stock',
        'תעודות סל': 'eft',
        'קרנות נאמנות': 'mf',
        'כתבי אופציה': 'warrants',
        'אופציות': 'options',
        'חוזים עתידיים': 'fc',
        'מוצרים מובנים': 'sp',
        'לא סחיר - תעודות התחייבות ממשלתי': 'ntgdc',
        'לא סחיר - תעודות התחייבות ממשלת': 'ntgdc',
        'לא סחיר - תעודות חוב מסחריות': 'ntcdc',
        'לא סחיר - אג"ח קונצרני': 'ntcb',
        'לא סחיר - מניות': 'ntstock',
        'לא סחיר - קרנות השקעה': 'ntif',
        'לא סחיר - כתבי אופציה': 'ntwarrants',
        'לא סחיר - אופציות': 'ntoptions',
        'לא סחיר - חוזים עתידיים': 'ntfc',
        'לא סחיר - מוצרים מובנים': 'ntsp',
        'הלוואות': 'loans',
        'פקדונות מעל 3 חודשים': 'dotm',
        'זכויות מקרקעין': 'lr',
        'השקעות אחרות': 'oi',
        'השקעה בחברות מוחזקות': 'ic',
        'יתרת התחייבות להשקעה': 'icb',
        'עלות מותאמת אג״ח קונצרני סחיר': 'cbac',
        'עלות מותאמת אג״ח קונצרני לא סחיר': 'cbac',
        'עלות מותאמת מסגרות אשראי ללווים': 'bcac',
    }

    CURRENCIES_LIST = [
        'דולר אוסטרליה',
        'ריאל ברזילאי',
        'דולר קנדי',
        'פרנק שוויצרי',
        'פסו ציליאני',
        'יואן סיני',
        'כתר דני',
        'אירו',
        'ליש"ט',
        'דולר הונג קונג',
        'פורינט הונגרי',
        'רופי הודי',
        'יין יפני',
        'פזו מכסיקני',
        'שקל חדש ישראלי',
        'כתר נורווגי',
        'ניו זילנד דולר',
        'זלוטי פולני',
        'רובל רוסי',
        'כתר שוודי',
        'דולר סינגפורי',
        'לירה טורקית',
        'דולר טיוואני',
        'דולר ארהב',
        'רנד דרא"פ',
        'UNKNOWN',
    ]

    INSTRUMENT_SUB_TYPE = [
        "תעודות התחייבות ממשלתיות",
        "תעודות חוב מסחריות",
        'אג"ח קונצרני',
        "מניות",
        "תעודות סל",
        "קרנות נאמנות",
        "קרנות מחקות",
        "כתבי אופציה",
        "אופציות",
        "חוזים עתידים",
        "מוצרים מובנים",
    ]

    RATING_AGENCIES = [
        'Moodys',
        'Moodys/מדרוג',
        'מדרוג',
        'S&P',
        'S&P/מעלות',
        'מעלות',
        'Fitch',
        'פנימי',
        # todo: tell to dniel.
        "מעלות/מדרוג",
    ]

    RATING_HASH = {
        'cb199856ed0bd04264a0ed400eacd5f9': ['Fitch', 'A'],
        '3190bbb8cb6382aa6b00fd9d4e2fab74': ['Fitch', 'A-'],
        'a62e38092b0138ca7ce03186f3f7c6d4': ['Fitch', 'A+'],
        'ecbdcea2bdbfffcc10cbf03b317a6dc5': ['Fitch', 'AA'],
        'd43737bf5942c787e2c8f994acb5e3a9': ['Fitch', 'AA-'],
        'fb5ccd6d6b50e6dc92288cda0b9649d3': ['Fitch', 'AA+'],
        '812d74c7dcea8c6e1394e5c5143e0e18': ['Fitch', 'AAA'],
        'b485009eec1b6737677774e7e7e4e160': ['Fitch', 'B'],
        '0ee09f47c2992461022684765369f4a7': ['Fitch', 'B-'],
        'd7b0ea7d366839fa3d17f48ee0691e88': ['Fitch', 'B+'],
        '5ce25f3f0ba4bbf082d71fc0eab16419': ['Fitch', 'BB'],
        '406300326a99c31607c0703343b71579': ['Fitch', 'BB-'],
        '0aa0c816c5d332db2982ab5764ffd004': ['Fitch', 'BB+'],
        '6d92af2a4cdddb7abb85f2ff5ffcd19a': ['Fitch', 'BBB'],
        'fedf0447887ab7dd94706ef78c9de56b': ['Fitch', 'BBB-'],
        'd30f512793235de1df22d47aa34f9ead': ['Fitch', 'BBB+'],
        'c1db550957764e343d341fd52d2522a1': ['Fitch', 'C'],
        '6fe6a59cb4134a1e43c86c9c0d864a68': ['Fitch', 'C-'],
        '0f142581f1f4c64db9f1c65dea70f939': ['Fitch', 'C+'],
        'f078bdaef01f0370a558bb2d00aa8ad7': ['Fitch', 'CC'],
        '8ff9b109d764d2049ddc59500aae04b0': ['Fitch', 'CCC'],
        '6186311d05d01b38b43e39bb1d5cee02': ['Fitch', 'CCC-'],
        '77df3341568f4ee7ee334f31b4d09564': ['Fitch', 'CCC+'],
        '3e17d31496e6739af3cddcdb5757112f': ['Fitch', 'D'],
        'd0ac4d02bc2b2ce14e5ba46f33de9a50': ['Fitch', 'N/R'],
        '3d2f0af471b3b7335933b9de9f9e9fa0': ['Fitch', 'nr'],
        'ae77f29ef821c9fc6bae205f5994a4c9': ['Fitch', 'NR1'],
        'd2382a87489ec80996826bf743baa7b5': ['Fitch', 'NR2'],
        '4dbaf128e1db5e56f4df6134568cd6c6': ['Fitch', 'nr3'],
        '75a04dfa1af7f4da441703177747b579': ['Fitch', 'לא דורג'],
        'ab5f40a00dcb590198e7b287000bda3b': ['Fitch', 'לא מדורג'],
        '1cd09eb250c49422c7b9dfe90ec561c9': ['Fitch', 'ללא דירוג'],
        'd4a923085880343ee575696afdfc93bc': ['Moodys', 'A1'],
        '993a29dfd64e762d845f9aede763224a': ['Moodys', 'A2'],
        'c54d2a00039645b7d834a67bcb5a1fc5': ['Moodys', 'A3'],
        'ab57bd1261e061e950ca43b0df648280': ['Moodys', 'Aa1'],
        'c8df2075e5b1be48637844aa039de7a1': ['Moodys', 'Aa2'],
        '292099b648b2f435d6289b6ced3054d8': ['Moodys', 'Aaa'],
        '35bb1b012af0d0e661600a44bf9fcb8c': ['Moodys', 'B1'],
        '450556b093b364935e3767fe132753b4': ['Moodys', 'B2'],
        '654d6761f998c7f9a5be125c97d4629e': ['Moodys', 'B3'],
        '87e8693d925061c3cc55facee2d1ae24': ['Moodys', 'Ba1'],
        'c20207db7a79a8f9774dab07cafc0196': ['Moodys', 'Ba2'],
        '987bf2071207824b39d4f87310a556de': ['Moodys', 'Ba3'],
        '11329636e35ab24fefafec895c448c2d': ['Moodys', 'Baa1'],
        '3510e07c1174ce81b67b93c20985e68a': ['Moodys', 'Baa2'],
        '89d46f8adb23b1f01d6d0284c78dd9a9': ['Moodys', 'Baa3'],
        '62fed2ffc04601ca2d6ec3efa5ce5dcd': ['Moodys', 'C'],
        '3189e210589bc8bf6b36b18fcb8d4eb5': ['Moodys', 'Ca'],
        'f4a256e757937602ad0a56725480e2b8': ['Moodys', 'Caa1'],
        'c24c9e89c9f109fdbca6a36c707facb3': ['Moodys', 'Caa2'],
        '4a1a604e77e397976d5ec6de5b8c3659': ['Moodys', 'Caa3'],
        '12362e1a1b7b96f07ba5ceab2e299ec0': ['Moodys', 'N/R'],
        '4402c23bd2568ba8102b06111614ef2a': ['Moodys', 'nr'],
        '5fd16341fc7d13365e5fe5f68a67f6ba': ['Moodys', 'NR1'],
        '6711f7f0324b85cff08e9c0afecc1dcf': ['Moodys', 'NR2'],
        'daebad3a856de8fbe5e063688a48f480': ['Moodys', 'nr3'],
        'ea38b8ce924859f341dc71d11d975ba4': ['Moodys', 'לא דורג'],
        '1abaca543a5b2b553302df7768b9301d': ['Moodys', 'לא מדורג'],
        '191871b4ec78ddeed6c1aa3540d485ac': ['Moodys', 'ללא דירוג'],
        'c190b4aa1dcba96c319e5a816a095b21': ['S&P', 'A'],
        '75e56be5fe1a0a8043e34e7a6647016d': ['S&P', 'A-'],
        'b92f9ca3e9e15624fbb0540790af4e3d': ['S&P', 'A+'],
        '6913cd439798755edba3fb9a087dcafc': ['S&P', 'AA'],
        '36f764bde7907a9ba61496924ad2a26c': ['S&P', 'AA-'],
        '5aad26b77dbd16f53d2d2de81ad1311e': ['S&P', 'AA+'],
        'b480e38fc41ee0b418db0f7ee3332cac': ['S&P', 'AAA'],
        '631c475565ef358f49141755d51fa634': ['S&P', 'B'],
        '2016b5a98e500242af12afdd23f1bffc': ['S&P', 'B-'],
        '1fb7428159a5fed0b40ec557c9d9bced': ['S&P', 'B+'],
        'a1f2aa9ef4c757a76dbf5770343da27b': ['S&P', 'BB'],
        'c1b3d4e59637f8caddb2c3eac3814a14': ['S&P', 'BB-'],
        '4fe44ee9225b3dfad71e2190c68e707b': ['S&P', 'BB+'],
        '4a26c3e112036ab543f80ee7ed9474a7': ['S&P', 'BBB'],
        '0953b53c39b6f9d9ca8750112a20f5f9': ['S&P', 'BBB-'],
        '44020ae5cf115b0d8314b2ff23e7e0ae': ['S&P', 'BBB+'],
        'bc338ceeea0d7628358a9b64b106c567': ['S&P', 'C'],
        '79d38c6e8a4e6eb19bb5c7d7246de7a8': ['S&P', 'C-'],
        '5027f357cbaf14919538d491176a04a6': ['S&P', 'C+'],
        '0e91d8535b0e20c03898d165988b82dc': ['S&P', 'CC'],
        '97e5059414a901f001b04d095a84b9fc': ['S&P', 'CCC'],
        '705204d6593a742f819b389822b137d6': ['S&P', 'CCC-'],
        '4216bea647da7084683cb87c9b2a15c9': ['S&P', 'CCC+'],
        'fb59ebdbf2651f1220c50c6100b40cbe': ['S&P', 'D'],
        'e2bcdd487c5d691783574b41e01d9a02': ['S&P', 'N/R'],
        '1e55fc3c4e096543022f9bdd66f2510a': ['S&P', 'nr'],
        '8704f20b02603b5b4acf590d3058cc05': ['S&P', 'NR1'],
        '6e387a4ac1f9c38e323c238ebdcf3ac2': ['S&P', 'NR2'],
        '9474b31328a7af18f6422dffd122090b': ['S&P', 'nr3'],
        '376e81b6905095ff8148a1fe1b7d75d0': ['S&P', 'לא דורג'],
        'f9f69ab1b70c3f634a94a1151df6af03': ['S&P', 'לא מדורג'],
        '626eebd1e59fad1c660e3cd54b826c6f': ['S&P', 'ללא דירוג'],
        '1c4fc8e8cbfd5791e5e892074f3a8065': ['מדרוג', 'A1'],
        'd50cbc1b524b1b0181db6614de9c949a': ['מדרוג', 'A2'],
        '3cdd38dae6bbc9ac894e7aa095acd168': ['מדרוג', 'A3'],
        'e892f606eeaf4d1b9ac7d027bc66dfc0': ['מדרוג', 'Aa1'],
        '4d72c7de9937caea8ea8f186fe86c4aa': ['מדרוג', 'Aa2'],
        '099c2280355afa64cbb4b1a438caed1c': ['מדרוג', 'Aaa'],
        '24c8d839dfc2aaf467724a4f0145a79f': ['מדרוג', 'B1'],
        'c061dd736910cd421968b3e9cbdbc91f': ['מדרוג', 'B2'],
        '034662744f49845d01a161e460f7318a': ['מדרוג', 'B3'],
        'cb038a763ea7ab6729df43018128a8d6': ['מדרוג', 'Ba1'],
        '4081383b639670c9804ecbc259a81348': ['מדרוג', 'Ba2'],
        '4dffec1a69b20c9bd5017e759de08abd': ['מדרוג', 'Ba3'],
        '7f81cac8be968cfa45600cdf43e41e42': ['מדרוג', 'Baa1'],
        '25479cb2a255fd20fb877a662b35b7f5': ['מדרוג', 'Baa2'],
        'f7212a572ee4e27d9fd7465995c65f9a': ['מדרוג', 'Baa3'],
        '41881490a2218cbd91f913d23e901b58': ['מדרוג', 'C'],
        '37fd96e8ef9c63308751651573afce4e': ['מדרוג', 'Ca'],
        'e372dada7e06150db9f53fa1a149abbe': ['מדרוג', 'Caa1'],
        'd6e7ab341619048fc5a72dd743111277': ['מדרוג', 'Caa2'],
        'f763ca9725bcfcefcc03abf3acd7c66b': ['מדרוג', 'Caa3'],
        '55785089bbeb02fab4131e5a74648504': ['מדרוג', 'N/R'],
        '087c05e1117d6cc4e5c324006c9c74f9': ['מדרוג', 'nr'],
        '21dc2d20b2a86021d6a9c4f88737179b': ['מדרוג', 'NR1'],
        'c943d4b96eaaf3191125f63d92c2fa40': ['מדרוג', 'NR2'],
        'ef821024d82bec65a33329a340afa099': ['מדרוג', 'nr3'],
        'c4514380e66c6207b38710abd510d501': ['מדרוג', 'לא דורג'],
        '3ed8e1e80c539d16083503b50a5402fb': ['מדרוג', 'לא מדורג'],
        '4219d65d2fc697262c6ea9e6ffa87a28': ['מדרוג', 'ללא דירוג'],
        '987fef5c51edb7d64d6bbd8fed6864bd': ['מעלות', 'A'],
        '5d1feac4586b72ad4dab276c4f5fa2bd': ['מעלות', 'A-'],
        '001497efbb33932ea337195c14cfbb6a': ['מעלות', 'A+'],
        'd8d335698024d58e71b60600ce52cfa2': ['מעלות', 'AA'],
        'f4e0b2a0c04fd1a018f94b410b514aed': ['מעלות', 'AA-'],
        '36d21a86e082e95ecff033ce34afc62f': ['מעלות', 'AA+'],
        '2db7a30e85697141bc97451b39737f1f': ['מעלות', 'AAA'],
        '267692d841f651258a37f6cd74577ee8': ['מעלות', 'B'],
        '152821bf827e20a272ba06794072db8c': ['מעלות', 'B-'],
        '1fb597e13fa23f327cc7a33d8eee432c': ['מעלות', 'B+'],
        'ec68b876b4e780439a43211be90ac0b8': ['מעלות', 'BB'],
        'd5644e9b87b1d52eacd434397190ee75': ['מעלות', 'BB-'],
        '87722f191e3b533d1766d79d71be77e3': ['מעלות', 'BB+'],
        '0c89c97a0a6f1d6a38cbaf2990ee7b49': ['מעלות', 'BBB'],
        '188aa3d105268f1a71e97c30cdee8ca2': ['מעלות', 'BBB-'],
        '2f245ca56c8a0f8c9a0e70abcc7d1b48': ['מעלות', 'BBB+'],
        '264c0a6cbed734279f57e995388e5123': ['מעלות', 'C'],
        '8793eff5b186acdc819314883e6465cf': ['מעלות', 'C-'],
        'fe6e365a069f9c03be52472aed5136e2': ['מעלות', 'C+'],
        '38c889ab267d4747d8ecf5fb6554c3ba': ['מעלות', 'CC'],
        '63d79d06ad94d42ae787ae6f3482ff7f': ['מעלות', 'CCC'],
        '6b78377be6ed36d009002dc5f00ddc69': ['מעלות', 'CCC-'],
        '23ff76a818022b5623fc2ad6f38c5b04': ['מעלות', 'CCC+'],
        '86923c9de89abed4b1c29961170eab66': ['מעלות', 'D'],
        '75494a604ad1d39ad6737da55430dd56': ['מעלות', 'N/R'],
        '0bf331163649cc6e131f5f27384c315e': ['מעלות', 'nr'],
        '3e6ff88edbb58ccebe6d0fe2f96b57c7': ['מעלות', 'NR1'],
        '376fefaae2c2e75848fd51025513398e': ['מעלות', 'NR2'],
        '938cca2257c91b0c730deb40bf77e019': ['מעלות', 'nr3'],
        '253e9d872d5b039b21379e909c903751': ['מעלות', 'לא דורג'],
        'c6d65766197a5d87374341bcd1756fa8': ['מעלות', 'לא מדורג'],
        'e6820f97a6c36d6a13b4e910d682f1b8': ['מעלות', 'ללא דירוג'],
        'e829cba4451262942129fdcd338eeb3b': ['מעורב', 'A'],
        'ff4cde6c6136a0f7066ddbf424dc3ff6': ['מעורב', 'A-'],
        'cca349e4e7337452521fdcf92300995c': ['מעורב', 'A+'],
        '95fe5d7ccdb3435b24d7c248a3c1060e': ['מעורב', 'AA'],
        '618befcdb8b1131b45ec8c8daa70e129': ['מעורב', 'AA-'],
        '731a3a33ba0aeb3eb51822bc9263ccd6': ['מעורב', 'AA+'],
        '9537c0e89de59286a5111f481068e450': ['מעורב', 'AAA'],
        '5adbd98e1854845114951ca17b0dba53': ['מעורב', 'B'],
        '96439b452fa836eaf3ab7fa6e7fbeebb': ['מעורב', 'B-'],
        '8ece6698e97e8f9777793e8c0f982b35': ['מעורב', 'B+'],
        '073e8aa77018aa14e04cf506c651bf32': ['מעורב', 'BB'],
        'e11cbfe6ea5e3e519e359a61dadb022c': ['מעורב', 'BB-'],
        '4a4a1a6c18bbeec896aa41ab1b788fc5': ['מעורב', 'BB+'],
        '4062c58e2f5118259361bae145d00d88': ['מעורב', 'BBB'],
        'f84a11dc942df1244041a1fc7e30c159': ['מעורב', 'BBB-'],
        '473d8838dea41e89e45d09fa97df2c52': ['מעורב', 'BBB+'],
        'd3218799d2e5d62752a16c5a7da0d7b9': ['מעורב', 'C'],
        'b3bf65a4022909e505f05295a33cd095': ['מעורב', 'C-'],
        '2175fba826c55a1abfcea762c1587a6f': ['מעורב', 'C+'],
        '78e17f8a728cc72ccf7950a9c6fc818d': ['מעורב', 'CC'],
        'e4eb8f93224f47a97008ebb7f0425226': ['מעורב', 'CCC'],
        '998de7ae93656daa11c7a41f495bd45d': ['מעורב', 'CCC-'],
        '755731ab38f2d208d3a578aeb1a9fd01': ['מעורב', 'CCC+'],
        '1b549a70295b8209e61a8bd32369eadc': ['מעורב', 'D'],
        '96c8967b4a2313f3a6b1a3c85dec076b': ['מעורב', 'N/R'],
        '94639530b5af049da3ab4cad3a5a6082': ['מעורב', 'nr'],
        'c71d1641787efe6dc6956e1009f83a1e': ['מעורב', 'NR1'],
        '16b7d5af6180e03c29eed2c647f5f8e0': ['מעורב', 'NR2'],
        '6ada6921c18c883c73545831fce7089f': ['מעורב', 'nr3'],
        '29b627da364c776ff7495ad767b28c4f': ['מעורב', 'לא דורג'],
        'b7b1fad183978e8374effd4bae3bbd92': ['מעורב', 'לא מדורג'],
        '5a04d2b73462114b99fa9548b6aea27d': ['מעורב', 'ללא דירוג'],
        'b4d0440f828d5789b9f55415d1ea6526': ['מעורב', 'A1'],
        'c2886f1c13738c1d7a43d12b719df8f0': ['מעורב', 'A2'],
        '3639d75b291490f23d0269f771ef8bd2': ['מעורב', 'A3'],
        '8185afc36fe45b8cfc5b9711ccfaa910': ['מעורב', 'Aa1'],
        '6a95c051fb0fa5cbbe3bf028baeed32d': ['מעורב', 'Aa2'],
        'c426882426e550b498fc6414e277f1f8': ['מעורב', 'Aaa'],
        '64b635e047d4f4409f3e2a6150289698': ['מעורב', 'B1'],
        '82ee39943571ef9948a88445f653cd25': ['מעורב', 'B2'],
        '2043567fa0604ad85338607317940e13': ['מעורב', 'B3'],
        '07138cae7ea3b4c91cc53dc3c863c40f': ['מעורב', 'Ba1'],
        'd0d533fb094c58fbd270eb9915732513': ['מעורב', 'Ba2'],
        'c755a03ceb1fa239e08f616b0affa0f7': ['מעורב', 'Ba3'],
        '2a569a1848c675e39f513fc5b3a28c00': ['מעורב', 'Baa1'],
        '0ff1fa71b59b751660fbce4cf17139a7': ['מעורב', 'Baa2'],
        'bf6599e7fb24b49cfc61244b9cf55399': ['מעורב', 'Baa3'],
        '38c70e8838be89cc718570a4d4baa461': ['מעורב', 'Ca'],
        '2ae3e52058a5a3028c93c1772b09eba9': ['מעורב', 'Caa1'],
        'eb594d3456aeb1d7125f79488fb829c3': ['מעורב', 'Caa2'],
        'e87f5837022666e8de99f49dcc9048d0': ['מעורב', 'Caa3'],
    }