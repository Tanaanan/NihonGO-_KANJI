def Getdetail():
    kanji_data = {
    '一': {
        'Meaning': 'one',
        'Onyoumi': 'いち (ichi)',
        'Kunyoumi': 'ひと(つ) (hito(tsu))',
        'Strokes': 1,
        'Reference': 'https://jisho.org/search/%E4%B8%80%20%23kanji'
    },
    '七': {
        'Meaning': 'seven',
        'Onyoumi': 'しち (shichi)',
        'Kunyoumi': 'なな(つ) (nana(tsu))',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E4%B8%83%20%23kanji'
    },
    '万': {
        'Meaning': 'ten thousand',
        'Onyoumi': 'まん (man)',
        'Kunyoumi': 'よろず(yorozu)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E4%B8%87%20%23kanji'
    },
    '三': {
        'Meaning': 'three',
        'Onyoumi': 'さん (san)',
        'Kunyoumi': 'み(つ) (mitsu)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E4%B8%89%20%23kanji'
    },
    '上': {
        'Meaning': 'above',
        'Onyoumi': 'じょう (jou)',
        'Kunyoumi': 'うえ (ue)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E4%B8%8A%20%23kanji'
    },
    '下': {
        'Meaning': 'below',
        'Onyoumi': 'か (ka)',
        'Kunyoumi': 'した (shita)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E4%B8%8B%20%23kanji'
    },
    '中': {
        'Meaning': 'middle',
        'Onyoumi': 'ちゅう (chuu)',
        'Kunyoumi': 'なか (naka)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E4%B8%AD%20%23kanji'
    },
    '九': {
        'Meaning': 'nine',
        'Onyoumi': 'きゅう (kyuu)',
        'Kunyoumi': 'ここの(つ) (kokonotsu)',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E4%B9%9D%20%23kanji'
    },
    '二': {
        'Meaning': 'two',
        'Onyoumi': 'に (ni)',
        'Kunyoumi': 'ふた(つ) (futa(tsu))',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E4%BA%8C%20%23kanji'
    },
    '五': {
        'Meaning': 'five',
        'Onyoumi': 'ご (go)',
        'Kunyoumi': 'いつ(つ) (itsu(tsu))',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E4%BA%94%20%23kanji'
    },
    '人': {
        'Meaning': 'person',
        'Onyoumi': 'じん (jin)',
        'Kunyoumi': 'ひと (hito)',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E4%BA%BA%20%23kanji'
    },
    '今': {
        'Meaning': 'now',
        'Onyoumi': 'こん (kon)',
        'Kunyoumi': 'いま (ima)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E4%BB%8A%20%23kanji'
    },
    '休': {
        'Meaning': 'rest',
        'Onyoumi': 'きゅう (kyuu)',
        'Kunyoumi': 'やす(む) (yasu(mu))',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E4%BC%91%20%23kanji'
    },
    '何': {
        'Meaning': 'what',
        'Onyoumi': 'か (ka)',
        'Kunyoumi': 'なに (nani)',
        'Strokes': 7,
        'Reference': 'https://jisho.org/search/%E4%BD%95%20%23kanji'
    },
    '先': {
        'Meaning': 'previous',
        'Onyoumi': 'せん (sen)',
        'Kunyoumi': 'さき (saki)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E5%85%88%20%23kanji'
    },
    '入': {
        'Meaning': 'enter',
        'Onyoumi': 'にゅう (nyuu)',
        'Kunyoumi': 'はい(る) (hairu)',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E5%85%A5%20%23kanji'
    },
    '八': {
        'Meaning': 'eight',
        'Onyoumi': 'はち (hachi)',
        'Kunyoumi': 'や(つ) (ya(tsu))',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E5%85%AB%20%23kanji'
    },
    '六': {
        'Meaning': 'six',
        'Onyoumi': 'ろく (roku)',
        'Kunyoumi': 'む(つ) (mu(tsu))',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%85%AD%20%23kanji'
    },
    '円': {
        'Meaning': 'circle',
        'Onyoumi': 'えん (en)',
        'Kunyoumi': 'まる(い) (marui)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%86%86%20%23kanji'
    },
    '出': {
        'Meaning': 'exit',
        'Onyoumi': 'しゅつ (shutsu)',
        'Kunyoumi': 'で(る) (deru)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%87%BA%20%23kanji'
    },
    '分': {
        'Meaning': 'minute',
        'Onyoumi': 'ぶん (bun)',
        'Kunyoumi': 'わ(ける) (wakeru)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%88%86%20%23kanji'
    },
    '前': {
        'Meaning': 'front',
        'Onyoumi': 'ぜん (zen)',
        'Kunyoumi': 'まえ (mae)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E5%89%8D%20%23kanji'
    },
    '北': {
        'Meaning': 'north',
        'Onyoumi': 'ほく (hoku)',
        'Kunyoumi': 'きた (kita)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%8C%97%20%23kanji'
    },
    '十': {
        'Meaning': 'ten',
        'Onyoumi': 'じゅう (juu)',
        'Kunyoumi': 'とお (too)',
        'Strokes': 2,
        'Reference': 'https://jisho.org/search/%E5%8D%81%20%23kanji'
    },
    '千': {
        'Meaning': 'thousand',
        'Onyoumi': 'せん (sen)',
        'Kunyoumi': 'ち (chi)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%8D%83%20%23kanji'
    },
    '午': {
        'Meaning': 'noon',
        'Onyoumi': 'ご (go)',
        'Kunyoumi': 'うま (uma)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%8D%88%20%23kanji'
    },
    '半': {
        'Meaning': 'half',
        'Onyoumi': 'はん (han)',
        'Kunyoumi': 'なか(ば) (nakaba)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%8D%8A%20%23kanji'
    },
    '南': {
        'Meaning': 'south',
        'Onyoumi': 'なん (nan)',
        'Kunyoumi': 'みなみ (minami)',
        'Strokes': 9,
        'Reference': 'https://jisho.org/search/%E5%8D%97%20%23kanji'
    },
    '友': {
        'Meaning': 'friend',
        'Onyoumi': 'ゆう (yuu)',
        'Kunyoumi': 'とも (tomo)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%8F%8B%20%23kanji'
    },
    '右': {
        'Meaning': 'right',
        'Onyoumi': 'う (u)',
        'Kunyoumi': 'みぎ (migi)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%8F%B3%20%23kanji'
    },
    '名': {
        'Meaning': 'name',
        'Onyoumi': 'めい (mei)',
        'Kunyoumi': 'な (na)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E5%90%8D%20%23kanji'
    },
    '四': {
        'Meaning': 'four',
        'Onyoumi': 'し (shi)',
        'Kunyoumi': 'よん (yon)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%9B%9B%20%23kanji'
    },
    '国': {
        'Meaning': 'country',
        'Onyoumi': 'こく (koku)',
        'Kunyoumi': 'くに (kuni)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E5%9B%BD%20%23kanji'
    },
    '土': {
        'Meaning': 'ground',
        'Onyoumi': 'ど (do)',
        'Kunyoumi': 'つち (tsuchi)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%9C%9F%20%23kanji'
    },
    '外': {
        'Meaning': 'outside',
        'Onyoumi': 'がい (gai)',
        'Kunyoumi': 'そと (soto)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%A4%96%20%23kanji'
    },
    '大': {
        'Meaning': 'big',
        'Onyoumi': 'だい (dai)',
        'Kunyoumi': 'おお(きい) (ookii)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%A4%A7%20%23kanji'
    },
    '天': {
        'Meaning': 'heaven',
        'Onyoumi': 'てん (ten)',
        'Kunyoumi': 'あま (ama)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E5%A4%A9%20%23kanji'
    },
    '女': {
        'Meaning': 'woman',
        'Onyoumi': 'じょ (jo)',
        'Kunyoumi': 'おんな (onna)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%A5%B3%20%23kanji'
    },
    '子': {
        'Meaning': 'child',
        'Onyoumi': 'し (shi)',
        'Kunyoumi': 'こ (ko)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%AD%90%20%23kanji'
    },
    '学': {
        'Meaning': 'study',
        'Onyoumi': 'がく (gaku)',
        'Kunyoumi': 'まな(ぶ) (manabu)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E5%AD%A6%20%23kanji'
    },
    '小': {
        'Meaning': 'small',
        'Onyoumi': 'しょう (shou)',
        'Kunyoumi': 'ちい(さい) (chiisai)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%B0%8F%20%23kanji'
    },
    '山': {
        'Meaning': 'mountain',
        'Onyoumi': 'さん (san)',
        'Kunyoumi': 'やま (yama)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%B1%B1%20%23kanji'
    },
    '川': {
        'Meaning': 'river',
        'Onyoumi': 'せん (sen)',
        'Kunyoumi': 'かわ (kawa)',
        'Strokes': 3,
        'Reference': 'https://jisho.org/search/%E5%B7%9D%20%23kanji'
    },
    '左': {
        'Meaning': 'left',
        'Onyoumi': 'さ (sa)',
        'Kunyoumi': 'ひだり (hidari)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E5%B7%A6%20%23kanji'
    },
    '年': {
        'Meaning': 'year',
        'Onyoumi': 'ねん (nen)',
        'Kunyoumi': 'とし (toshi)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E5%B9%B4%20%23kanji'
    },
    '後': {
        'Meaning': 'after',
        'Onyoumi': 'ご (go)',
        'Kunyoumi': 'あと (ato)',
        'Strokes': 9,
        'Reference': 'https://jisho.org/search/%E5%BE%8C%20%23kanji'
    },
    '日': {
        'Meaning': 'day',
        'Onyoumi': 'にち (nichi)',
        'Kunyoumi': 'ひ (hi)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E6%97%A5%20%23kanji'
    },
    '明': {
        'Meaning': 'bright',
        'Onyoumi': 'めい (mei)',
        'Kunyoumi': 'あかり (akari)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E6%98%8E%20%23kanji'
    },
    '時': {
        'Meaning': 'time',
        'Onyoumi': 'じ (ji)',
        'Kunyoumi': 'とき (toki)',
        'Strokes': 10,
        'Reference': 'https://jisho.org/search/%E6%99%82%20%23kanji'
    },
    '書': {
        'Meaning': 'write',
        'Onyoumi': 'しょ (sho)',
        'Kunyoumi': 'か(く) (kaku)',
        'Strokes': 10,
        'Reference': 'https://jisho.org/search/%E6%9B%B8%20%23kanji'
    },
    '月': {
        'Meaning': 'moon',
        'Onyoumi': 'げつ (getsu)',
        'Kunyoumi': 'つき (tsuki)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E6%9C%88%20%23kanji'
    },
    '木': {
        'Meaning': 'tree',
        'Onyoumi': 'もく (moku)',
        'Kunyoumi': 'き (ki)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E6%9C%A8%20%23kanji'
    },
    '本': {
        'Meaning': 'book',
        'Onyoumi': 'ほん (hon)',
        'Kunyoumi': 'もと (moto)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E6%9C%AC%20%23kanji'
    },
    '来': {
        'Meaning': 'come',
        'Onyoumi': 'らい (rai)',
        'Kunyoumi': 'く(る) (kuru)',
        'Strokes': 7,
        'Reference': 'https://jisho.org/search/%E6%9D%A5%20%23kanji'
    },
    '東': {
        'Meaning': 'east',
        'Onyoumi': 'とう (tou)',
        'Kunyoumi': 'ひがし (higashi)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E6%9D%B1%20%23kanji'
    },
    '校': {
        'Meaning': 'school',
        'Onyoumi': 'こう (kou)',
        'Kunyoumi': 'やしろ (yashiro)',
        'Strokes': 10,
        'Reference': 'https://jisho.org/search/%E6%A0%A1%20%23kanji'
    },
    '母': {
        'Meaning': 'mother',
        'Onyoumi': 'ぼ (bo)',
        'Kunyoumi': 'はは (haha)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E6%AF%8D%20%23kanji'
    },
    '毎': {
        'Meaning': 'every',
        'Onyoumi': 'まい (mai)',
        'Kunyoumi': 'ごと (goto)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E6%AF%8E%20%23kanji'
    },
    '気': {
        'Meaning': 'spirit',
        'Onyoumi': 'き (ki)',
        'Kunyoumi': 'いき (iki)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E6%B0%97%20%23kanji'
    },
    '水': {
        'Meaning': 'water',
        'Onyoumi': 'すい (sui)',
        'Kunyoumi': 'みず (mizu)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E6%B0%B4%20%23kanji'
    },
    '火': {
        'Meaning': 'fire',
        'Onyoumi': 'か (ka)',
        'Kunyoumi': 'ひ (hi)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E7%81%AB%20%23kanji'
    },
    '父': {
        'Meaning': 'father',
        'Onyoumi': 'ふ (fu)',
        'Kunyoumi': 'ちち (chichi)',
        'Strokes': 4,
        'Reference': 'https://jisho.org/search/%E7%88%B6%20%23kanji'
    },
    '生': {
        'Meaning': 'life',
        'Onyoumi': 'せい (sei)',
        'Kunyoumi': 'い(きる) (ikiru)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E7%94%9F%20%23kanji'
    },
    '男': {
        'Meaning': 'man',
        'Onyoumi': 'だん (dan)',
        'Kunyoumi': 'おとこ (otoko)',
        'Strokes': 7,
        'Reference': 'https://jisho.org/search/%E7%94%B7%20%23kanji'
    },
    '白': {
        'Meaning': 'white',
        'Onyoumi': 'はく (haku)',
        'Kunyoumi': 'しろ (shiro)',
        'Strokes': 5,
        'Reference': 'https://jisho.org/search/%E7%99%BD%20%23kanji'
    },
    '百': {
        'Meaning': 'hundred',
        'Onyoumi': 'ひゃく (hyaku)',
        'Kunyoumi': 'もも (momo)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E7%99%BE%20%23kanji'
    },
    '聞': {
        'Meaning': 'hear',
        'Onyoumi': 'ぶん (bun)',
        'Kunyoumi': 'き(く) (kiku)',
        'Strokes': 14,
        'Reference': 'https://jisho.org/search/%E8%81%9E%20%23kanji'
    },
    '行': {
        'Meaning': 'go',
        'Onyoumi': 'こう (kou)',
        'Kunyoumi': 'い(く) (iku)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E8%A1%8C%20%23kanji'
    },
    '西': {
        'Meaning': 'west',
        'Onyoumi': 'せい (sei)',
        'Kunyoumi': 'にし (nishi)',
        'Strokes': 6,
        'Reference': 'https://jisho.org/search/%E8%A5%BF%20%23kanji'
    },
    '見': {
        'Meaning': 'see',
        'Onyoumi': 'けん (ken)',
        'Kunyoumi': 'み(る) (miru)',
        'Strokes': 7,
        'Reference': 'https://jisho.org/search/%E8%A6%8B%20%23kanji'
    },
    '話': {
        'Meaning': 'talk',
        'Onyoumi': 'わ (wa)',
        'Kunyoumi': 'はな(す) (hanasu)',
        'Strokes': 13,
        'Reference': 'https://jisho.org/search/%E8%A9%B1%20%23kanji'
    },
    '語': {
        'Meaning': 'word',
        'Onyoumi': 'ご (go)',
        'Kunyoumi': 'かた(る) (kataru)',
        'Strokes': 14,
        'Reference': 'https://jisho.org/search/%E8%AA%9E%20%23kanji'
    },
    '読': {
        'Meaning': 'read',
        'Onyoumi': 'どく (doku)',
        'Kunyoumi': 'よ(む) (yomu)',
        'Strokes': 14,
        'Reference': 'https://jisho.org/search/%E8%AA%AD%20%23kanji'
    },
    '車': {
        'Meaning': 'car',
        'Onyoumi': 'しゃ (sha)',
        'Kunyoumi': 'くるま (kuruma)',
        'Strokes': 7,
        'Reference': 'https://jisho.org/search/%E8%BB%8A%20%23kanji'
    },
    '金': {
        'Meaning': 'gold',
        'Onyoumi': 'きん (kin)',
        'Kunyoumi': 'か(ね) (kane)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E9%87%91%20%23kanji'
    },
    '長': {
        'Meaning': 'long',
        'Onyoumi': 'ちょう (chou)',
        'Kunyoumi': 'なが(い) (nagai)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E9%95%B7%20%23kanji'
    },
    '間': {
        'Meaning': 'interval',
        'Onyoumi': 'かん (kan)',
        'Kunyoumi': 'あいだ (aida)',
        'Strokes': 12,
        'Reference': 'https://jisho.org/search/%E9%96%93%20%23kanji'
    },
    '雨': {
        'Meaning': 'rain',
        'Onyoumi': 'う (u)',
        'Kunyoumi': 'あめ (ame)',
        'Strokes': 8,
        'Reference': 'https://jisho.org/search/%E9%9B%A8%20%23kanji'
    },
    '電': {
        'Meaning': 'electricity',
        'Onyoumi': 'でん (den)',
        'Kunyoumi': '',
        'Strokes': 13,
        'Reference': 'https://jisho.org/search/%E9%9B%BB%20%23kanji'
    },
    '食': {
        'Meaning': 'eat',
        'Onyoumi': 'しょく (shoku)',
        'Kunyoumi': 'た(べる) (taberu)',
        'Strokes': 9,
        'Reference': 'https://jisho.org/search/%E9%A3%9F%20%23kanji'
    },
    '高': {
        'Meaning': 'tall',
        'Onyoumi': 'こう (kou)',
        'Kunyoumi': 'たか(い) (takai)',
        'Strokes': 10,
        'Reference': 'https://jisho.org/search/%E9%AB%98%20%23kanji'
    }

    }
    return kanji_data