# மடக்கு வாக்கியம் (Loops)

அடிப்படையில் கணினியை பலமுறை ஒரு குறிப்பிட்ட சில கட்டளைகளை செய்ய முனைவது மடக்கு வாக்கியம். கணினி மனிதர்களை போல் இன்பம், வலி, பசி போன்ற உணர்வுகளுக்கு ஆளாகாததால் இந்த இயந்திரம் சளைக்காமல் வேலைகளை (கணக்குகளை) செய்யும் - அதற்க்கு "போர் (boredom)" அலுப்படையாமல் வேலைகளை செய்யும் திறன் கொண்டது.

ஒரு மடக்கு வாக்கியம் (loop "லூப்" என்று ஆங்கிலத்தில் சொல்வார்கள்) என்பது ஒரே செயலை (அல்லது சில குறிப்பிட்ட செயல்களை) பலமுறை திரும்ப திரும்ப செய்யும் பொருள் கொண்டது; கணினி ஒரு மின் இயந்திரம் என்பதால் கடகட என்று நொடிக்கு பல மில்லியன் "flops" (floating-point operations per second) என்ற வேகத்தில் நீங்கள் இட்ட மடக்கு வாக்கியம் சூழ்ந்த கட்டளைகளை கண்சிமிட்டும் நேரத்தில் இயக்கி முடிக்கும். கீழ் வரும் நிரல் துண்டை படித்து அதில் உள்ள "while" மடக்கு வாக்கியத்தை ஆராய்ந்து பார்க்கலாம் வாருங்கள்.

```ruby
x = 0
while x < 5
  puts x
  x = x + 1
end
puts "மடக்கு கட்டளை முடிந்தது"
```

 மடக்கு வாக்கியத்த ரூபி மொழியில் இந்த எடுத்துக்காட்டு விளக்கியது.  _while_ என்ற குறிச்சொல் அடுத்து வரும் மாறி 'true' (உண்மை) என்றவரை மட்டுமே இந்த மடக்கு வாக்கியம் தொடர்ந்து இயங்கும் -  இங்கு அது 
 x என்ற மாறியின் மதிப்பு 5 ஆகும் வரை இயங்கும். அதன் பின் மடக்கு கட்டளைகளில் இருந்து வெளியேறி 
 "மடக்கு கட்டளை முடிந்தது" என்ற செய்தியை அச்சிட்டு முடியும்.

மேல் கொடுக்கப்பட்ட மடக்கு வாக்கியம் ஒரு நிபந்தனை  
(x < 5)
உண்மையாக இருக்கும் வரை அதனுள் உள்ள எல்லா கட்டளைகளையும் இயக்கும்.உங்கள் பெற்றோர் நீங்க சாலையை தாண்டும் வரை இரண்டு பக்கமும் கவனம் செலுத்த சொல்வாங்க இல்லையா ? அதே போல தான் இந்த வரை எனும் _while_ கட்டளை செயல்படும். அதாவது உங்கள் பெற்றோர்கள் உங்களையே நிரல்படுத்துகிறது 
போல என்றும் சொல்லலாம் - அதாவது சாலையில் இரண்டு பக்கமும் கார்கள் இல்லாத வரை மட்டுமே நீங்கள் சாலையை கடக்கலாம்.

ரூபி கட்டளை  `puts` திரையில் அதனை சார்ந்த மதிப்பை அச்சிடும்; கொஞ்சம் நுட்பமாக சொல்லவேண்டுமானால் திரையில் அச்சிட 
`puts` என்ற கட்டளைக்கு ஒத்து வரும் மதிப்பை எடுத்துக்கொள்ளும் - அடுத்து இந்த மதிப்பு திரையில் அச்சாகும்!

கீழ் கண்ட மாதிரி கட்டளைகள் (pseudocode) என்பது _while_ மடக்கு வாக்கியம் எப்படி செயலாற்றும் என்று விளக்கும் வண்ணம் கொடுக்கப்பட்டது
```
# pseudo code
1) x is 0
2) Is 0 less than 5? True. puts x. x = 0 + 1. x is 1.
3) Is 1 less than 5? True. puts x. x = 1 + 1. x is 2.
4) Is 2 less than 5? True. puts x. x = 2 + 1. x is 3.
5) Is 3 less than 5? True. puts x. x = 3 + 1. x is 4.
6) Is 4 less than 5? True. puts x. x = 4 + 1. x is 5.
7) Is 5 less than 5? False. Loop ends.
8) "while மடக்கு வாக்கியம் முடிந்தது." is printed to the screen.
```

இந்த உதாரணத்தில் மாறி, x பூஜ்ஜியம் என்று தொடக்கத்தில் அதாவது,  மடக்கு வாக்கியத்தின் முன்பு, மதிப்பு பெறுகிறது. மடக்கு வாக்கியம் தொடங்கும் போது, கணினி இந்த மாறியின் மதிப்பு ஐந்திற்கு கம்மியாக இருக்கிறதா என்று பார்க்கும். பூஜ்ஜியம் என்பது ஐந்திற்கு கம்மியானது அதனால் திரையில் _puts_ இன் ஒத்த சரம் வெளியிடப்படும். மடக்கு வாக்கியத்தில் அடுத்த கட்டளை x என்பதன்
மதிப்பை ஒன்றால் கூட்டக்கூடியது. இதுபோலவே _x_ என்பதன் மதிப்பு 5 ஐ எட்டும் வரை தொடர்ந்து இயங்கும் - ஐந்தை எட்டியபின் மடக்கு 
வாக்கியம் முடிவடைந்து அடுத்த கட்டளைக்கு இயக்கம் செல்லும் - இங்கு இந்த கட்டளை _puts 

இதன் இயக்கம் வெளிப்பாடு இதுபோல் அமையும்:

```
0
1
2
3
4
while மடக்கு வாக்கியம் முடிந்தது.
```

![Art by Vixuong Hong](http://rubykin.com/images/roller-coaster.png)

<br />
_While_ மடக்கு வாக்கியங்களை வைத்து கொண்டு வெறும் எண்ணுவது மட்டுமே இதுவரை செய்துள்ளோம். அடுத்து இதே _while_ 
வாக்கியத்தை கொண்டு வேறென்ன ஒரு முடிவிலா இயக்கத்தை வடிவமைக்கலாம் என்று பாருங்கள். இந்த 
எடுத்துகாட்டில் சரியான சாரம் உள்ளீடு செய்யும் வரை இந்த _while_ மடக்கு வாக்கியம் இயங்கி கொண்டே இருக்கும். 

```ruby
answer = ""  #காலி சரம் ஒன்றை உருவாக்குங்கள் 
while answer != "Ruby"
  puts "மன்னிக்கவும் தவரான விடை." unless answer == ""
  puts "மிக சிறந்த கணினி மொழி எது?"
  answer = gets.chomp
end
puts "அடி சக்கை!"
```
இங்கு சில புதிய ரூபி சார்புகளை பயன்படுத்தினோம்; இவை : `gets` மற்றும் `chomp`. இவை இந்த புத்தகம் வாசிக்கும் அளவில் உங்களுக்கு விளக்க படும்.

**நிரல் விளக்கம்** 
மேல் உள்ள நிரல் துண்டு "மிக சிறந்த கணினி மொழி எது ?" என்ற கேள்விக்கு "Ruby" என்று ஆங்கிலத்தில் கொடுக்கும் வரை இயங்கிக்கொண்டே இருக்கும். உங்கள் உள்ளீடை _gets.chomp_ என்ற சார்பு பெற்று கொண்டு _answer_ என்ற மாறியில் சேமிக்கும்; இதனையே _while_ மடக்கு வாக்கியம் முடியும் வரை இயக்கிக்கொள்ளும்.

_chomp_ என்ற சார்பு கிடைத்த சாரத்தில் கடைசியில் உள்ள வரி முடிவு  எழுத்தான '\n' என்பதை 
அழித்து பயன்படுத்தும் வண்ணம் உங்களுக்கு அந்த சரத்தை பின் கொடுக்கும்.

உங்கள் நிரலை சரிவர  பயன்படுத்தும் பயனர் ,"Ruby" என்று கொடுத்ததும் இந்த மடக்கு வாக்கியத்தில் இருந்து வெளியேரும்
அதன் பின் "அடி சக்கை" என்று கொஞ்சம் எகத்தாளமாகவே நிரல்போல் திரையில் வெளியிட்டு முடிக்கும். 

அடுத்து இந்த எடுத்துக்காட்டில்  _for loop_ என்று சொல்லக்கூடிய ஒவ்வொன்றாக _for_ குறிச்சொல்லை கொண்ட மடக்கு வாக்கியத்தை பார்க்கலாம்.

```ruby
for number in 1..5 do
  puts "தற்போதைய மதிப்பு #{number}"
end
```

இந்த _for_ மடக்கு வாக்கியம் _while_ என்ற மடக்கு வாக்கியம் போல இல்லாமல் நிபந்தனை உண்மையாகாமல் இருந்தாலும் தொடங்கும். மேல் உள்ள நிரல் துண்டு 1-இல் இருந்து 5-வரை (மொத்தம் 5 முறை) இந்த puts நிரல் கட்டளையை இயக்கம். 

 இங்கு சிறப்பாக நீங்க கவனிக்க வேண்டியது, மாறி 'number' என்பது -
 இது மதிப்பு வாக்கியம் இயங்கும் பொழுது இதன் மதிப்பு 1, 2, 3, 4, 5 என மறி இக்கொண்டே
 போகும். இப்போது  _for_ மடக்கு வாக்கியத்தை இரண்டில் இருந்து எட்டு வரை, அதாவது ஏழு முறை [2,3,4,5,6,7,8] என இயக்க _2..8_ என்று ரூபி மொழியில் கொடுக்கலாம். இப்போது இதையே ஒன்றில் இருந்து இருபத்தைந்து வரை எப்படி எழுதுவீர்கள் 
 ? முயன்று பாருங்களேன்.
 
 _puts_ என்பது எப்படி ஓவொரு முறையும் தனது மதிப்பை மாற்றி கொள்கிறது ? இதற்க்கு காரணம் _number_ என்பது இடமாற்றம் அடைகிறது (substitution) - ஓவொரு முறை மடக்கு வாக்கியம் இயங்கும் சமயம் _number_ இதன் மதிப்பு மாறுகிறது, பின்பு இதன் இடம் மாற்றத்தால் _puts_ இன் மதிப்பும் மாறி திரையில் அச்சாகிறது.
```
தற்போதைய மதிப்பு 1
தற்போதைய மதிப்பு 2
தற்போதைய மதிப்பு 3
தற்போதைய மதிப்பு 4
தற்போதைய மதிப்பு 5
```

உங்களுக்கு ரூபியின் மடக்கு வாக்கியங்களின் பலம் புலப்படும் என்று நினைக்கிறோம். இங்கு கொடுக்கப்பட்ட ரூபி மடக்கு வாக்கியம் _while_ மற்றும் _for_ தவிர மற்றவையும் உள்ளன அனால் இதை கொண்டு மட்டுமே நாம் தொடக்கத்தில் இயங்கலாம். மடக்கு வாக்கியங்களை தரவமைப்புகளுடன் (datastructures) இணைந்து நிரல்படுத்தினால் இவற்றின் அசுர பலம் காணலாம்!

உங்களுக்கு ஒரு பொம்மை அலமாரி, அல்லது ஒரு சொப்பு சாமான் திரட்டு பரப்பி இருந்தால் இவற்றை எண்ணுவது, சரிபார்ப்பது, வரிசைப்படுத்துவது என்பதை எல்லாமே ரூபியிடம் ஒரு 
அதிவேக கணினியிடம் கொடுத்துவிடலாம். நீங்கள் இதை செய்யாமல் ஒரு செவ்வியல் புத்தகத்தையோ அல்லது தமிழிசை, கர்நாடக 
இசையை இரசிக்க நேரம் கழிக்கலாம், இல்லாட்டி ஒரு தலைவர் படத்தை கூட மறுபடி பார்க்கலாம். ரூபியின் மடக்கு வாக்கியங்கள் பலம் உங்களுக்கு எப்போதும் உண்டு! இந்த தொகுதியை முடிப்பதற்கு  

<div style="height:30px;"></div>
