# chatbox.py - Handles chatbot responses for livestock health

def get_chat_response(user_message):
    user_message = user_message.strip().lower()

    responses = {
        "hello": "Hi there How can I assist you with cattle health today?\nதமிழ்: வணக்கம் நீங்கள் மாடுகளின் ஆரோக்கியத்திற்கு உதவ விரும்புகிறீர்களா?",
        "hi": "Hello How can I help\nதமிழ்: ஹலோ நான் எவ்வாறு உதவலாம்?",
        "hey": "Hey Need any help with livestock care?\nதமிழ்: ஹேய் மாடுகளின் பராமரிப்பிற்கு ஏதாவது உதவி வேண்டுமா?",

        "what is livestock": "Livestock refers to domesticated animals raised in farms such as cows goats sheep and poultry for food milk and other products.\nதமிழ்: கால்நடைகள் என்பது பண்ணையில் வளர்க்கப்படும் மாடுகள் ஆடுகள் செம்மறியாடுகள் கோழிகள் போன்றவை ஆகும். இவை உணவு பால் மற்றும் பிற பொருட்களுக்கு பயன்படுத்தப்படுகின்றன.",

        "how to take care of cattle": "Proper cattle care includes providing clean water nutritious feed regular veterinary checkups proper shelter and vaccinations.\nதமிழ்: மாடுகளை சரியாக பராமரிப்பதற்கான முக்கிய அம்சங்கள் தூய்மையான நீர் ஊட்டச்சத்து நிறைந்த உணவு மிருக மருத்துவ பரிசோதனைகள் சரியான தங்குமிடம் மற்றும் தடுப்பூசிகள்.",

        "what is the best diet for cattle": "Cattle need a balanced diet of roughages hay silage concentrates grains minerals and fresh water.\nதமிழ்: மாடுகளுக்கு இருபால் உணவாக வைக்கோல் காய்ந்த பசு தீவனம் தானியங்கள் கனிமச்சத்து மற்றும் புதிய நீர் தேவை.",

        "how often should cattle be vaccinated": "Cattle should be vaccinated regularly following a vet-recommended schedule including vaccines for LSD FMD and BVD.\nதமிழ்: மாடுகளுக்கு LSD FMD BVD போன்ற முக்கியமான தடுப்பூசிகளை மிருக மருத்துவ ஆலோசனைப்படி முறையாக போட வேண்டும்.",

        "what is lsd": "Lumpy Skin Disease LSD is a viral disease in cattle that causes skin nodules fever and reduced milk production.\nதமிழ்: லம்பி ஸ்கின் நோய் (LSD) என்பது மாடுகளில் தோல் முடிச்சுகள் காய்ச்சல் மற்றும் பாலின் உற்பத்தி குறைவதற்கு காரணமாகும்.",

        "what are the symptoms of lsd": "Symptoms include fever skin nodules swelling of limbs nasal discharge and weight loss.\nதமிழ்: LSD நோயின் அறிகுறிகளில் காய்ச்சல் தோலில் முடிச்சுகள் கால்களில் வீக்கம் மூக்கிலிருந்து வெளிப்படும் திரவம் மற்றும் உடல் எடை குறைதல் அடங்கும்.",

        "how does lsd spread": "LSD spreads through insect bites contaminated feed and close contact with infected cattle.\nதமிழ்: LSD பூச்சிக்கடிகள் மாசுபட்ட தீவனம் மற்றும் பாதிக்கப்பட்ட மாடுகளுடன் நேரடி தொடர்பு மூலம் பரவுகிறது.",

        "how to prevent lsd": "Prevention includes vaccination insect control proper sanitation and isolation of infected animals.\nதமிழ்: தடுப்பு முறையில் தடுப்பூசி பூச்சிக்கொல்லுதல் சுத்தமான சூழல் மற்றும் பாதிக்கப்பட்ட மாடுகளை தனிமைப்படுத்துதல் அடங்கும்.",

        "is lsd fatal": "LSD is rarely fatal but causes economic losses due to reduced milk yield and slow recovery.\nதமிழ்: LSD மிக குறைந்த அளவில் உயிருக்கு ஆபத்தை ஏற்படுத்தும் ஆனால் பாலின் உற்பத்தி குறைவதால் வேளாண் நஷ்டம் அதிகரிக்கிறது.",

        "is there a cure for lsd": "There is no direct cure but supportive care like antibiotics for secondary infections and pain relievers helps recovery.\nதமிழ்: LSDக்கு நேரடி மருந்தில்லை ஆனால் துணை சிகிச்சைகள் антибиотிக்கள் மற்றும் வலி நிவாரணி மருந்துகள் குணமாக உதவுகிறது.",

        "lsd vaccine name": "LSD vaccines include Neethling strain vaccine and Homologous LSDV vaccine.\nதமிழ்: LSDக்கு Neethling strain vaccine மற்றும் Homologous LSDV vaccine போன்ற தடுப்பூசிகள் உள்ளன.",

        "what are the stages of lsd": "LSD has three stages Incubation (5-14 days) Acute phase (visible skin nodules) and Recovery phase (scarring and healing).\nதமிழ்: LSDக்கு மூன்று நிலைகள் உள்ளன: முடங்கிய நிலை (5-14 நாட்கள்), தீவிர நிலை (தோலில் முடிச்சுகள் தென்படும்) மற்றும் மீட்சி நிலை (முடிச்சுகள் மறைந்து குணமாதல்).",

        "how to prevent cattle diseases": "Vaccination hygiene insect control and balanced nutrition help prevent most diseases.\nதமிழ்: தடுப்பூசிகள் தூய்மை பூச்சிக்கொல்லுதல் மற்றும் சரியான உணவு முறை மூலம் பெரும்பாலான நோய்களைத் தடுக்கலாம்.",

        "how to increase milk production in cows": "Provide high-quality feed regular water clean milking conditions and proper rest.\nதமிழ்: உயர்தர தீவனம் புதிய நீர் தூய்மையான பால் பறிப்பு சூழல் மற்றும் போதிய ஓய்வு மூலம் பாலின் உற்பத்தியை அதிகரிக்கலாம்.",

        "can humans get lsd from cattle": "No LSD does not spread to humans It only affects cattle.\nதமிழ்: இல்லை LSD மனிதர்களுக்கு பரவாது இது மாடுகளை மட்டுமே பாதிக்கிறது.",

        "does lsd affect milk quality": "Yes LSD reduces milk yield and infected cows should not be milked until recovery.\nதமிழ்: ஆம் LSD பாலின் உற்பத்தியை குறைக்கிறது மற்றும் பாதிக்கப்பட்ட மாடுகளிலிருந்து பாலை எடுத்துக் கொள்ளக்கூடாது.",

        "default": "I'm sorry I didn't understand that Can you please rephrase your question?\nதமிழ்: மன்னிக்கவும் நீங்கள் கேட்ட கேள்வியை நான் புரிந்துகொள்ளவில்லை தயவுசெய்து மறு கூறுங்கள்."
    }

    return responses.get(user_message, responses["default"])
