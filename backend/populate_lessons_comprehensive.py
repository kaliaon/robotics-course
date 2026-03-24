#!/usr/bin/env python
"""
Comprehensive script to populate the database with lesson data for the "Fundamentals of Robotics" course.

This script should be run from the project root directory using:
python populate_lessons_comprehensive.py
"""

import os
import django
import random
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses_platform.settings')
django.setup()

from courses.models import Course, Lesson, Test, Question, Choice, QuestionType
from django.db import connection

def create_quiz_questions(title, subject, num_questions=3):
    """Create natural quiz questions for a lesson with correct answers for open-ended questions."""
    questions = []
    
    # Define realistic questions based on the subject (Robotics)
    # Generic templates for fallback if specific questions aren't defined
    realistic_questions = {
        "Тинкеркадпен танысу": [
            {
                "text": "Tinkercad дегеніміз не?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "3D модельдеу және электрониканы симуляциялауға арналған онлайн платформа", "is_correct": True},
                    {"text": "Тек мәтіндік редактор", "is_correct": False},
                    {"text": "Күрделі инженерлік есептеулерге арналған бағдарлама", "is_correct": False},
                    {"text": "Әлеуметтік желі", "is_correct": False}
                ]
            },
            {
                "text": "Tinkercad-та схема құрастыру үшін қандай бөлімді таңдау керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Circuits (Схемалар)", "is_correct": True},
                    {"text": "3D Designs", "is_correct": False},
                    {"text": "Codeblocks", "is_correct": False},
                    {"text": "Lessons", "is_correct": False}
                ]
            },
            {
                "text": "Tinkercad платформасының негізгі артықшылығы неде?",
                "type": "question_type_OPEN",
                "correct_answer": "Орнатуды қажет етпейді, браузер арқылы жұмыс істейді, тегін және жаңадан бастаушыларға өте ыңғайлы."
            }
        ],
        "Ардуино және Макеталық тақша": [
            {
                "text": "Arduino дегеніміз не?",
                "type": "question_type_OPEN",
                "correct_answer": "Arduino - бұл қарапайым автоматтандырылған жүйелер мен роботтехниканы жасауға арналған аппараттық-бағдарламалық құрал."
            },
            {
                "text": "Макеталық тақша (Breadboard) не үшін қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Дәнекерлеусіз прототиптерді жылдам жинау үшін", "is_correct": True},
                    {"text": "Тек микросхемаларды сақтау үшін", "is_correct": False},
                    {"text": "Ток көзі ретінде", "is_correct": False},
                    {"text": "Дайын құрылғыны бекіту үшін", "is_correct": False}
                ]
            },
            {
                "text": "Arduino UNO платасында қандай микроконтроллер қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "ATmega328P", "is_correct": True},
                    {"text": "Intel Core i7", "is_correct": False},
                    {"text": "STM32", "is_correct": False},
                    {"text": "ESP8266", "is_correct": False}
                ]
            }
        ],
        "Жарық диоды": [
            {
                "text": "Жарық диодының (LED) ұзын аяқшасы нені білдіреді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Анод (оң, +)", "is_correct": True},
                    {"text": "Катод (теріс, -)", "is_correct": False},
                    {"text": "Жер (GND)", "is_correct": False},
                    {"text": "Сигнал", "is_correct": False}
                ]
            },
            {
                "text": "Жарық диодын Arduino-ға тікелей қосқанда неге резистор қажет?",
                "type": "question_type_OPEN",
                "correct_answer": "Жарық диоды күйіп кетпеуі үшін токты шектеу мақсатында резистор қолданылады."
            }
        ],
        "Алғашқы бағдарлама": [
            {
                "text": "Arduino бағдарламасындағы setup() функциясы не үшін қажет?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Баптауларды орнату үшін, бір рет орындалады", "is_correct": True},
                    {"text": "Циклдік қайталау үшін", "is_correct": False},
                    {"text": "Кітапханаларды қосу үшін", "is_correct": False},
                    {"text": "Айнымалыларды жариялау үшін", "is_correct": False}
                ]
            },
            {
                "text": "loop() функциясының қызметі қандай?",
                "type": "question_type_OPEN",
                "correct_answer": "Негізгі кодты шексіз қайталап орындау үшін қолданылады."
            }
        ],
        "Бағдаршам": [
            {
                "text": "Arduino-дағы delay(1000) командасы нені білдіреді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Бағдарламаны 1000 миллисекундқа (1 секунд) кідірту", "is_correct": True},
                    {"text": "Жарықты 1000 есе күшейту", "is_correct": False},
                    {"text": "Бағдарламаны 1000 рет қайталау", "is_correct": False},
                    {"text": "1000 пинді іске қосу", "is_correct": False}
                ]
            },
            {
                "text": "Бағдаршам жобасында қандай түсті LED-тер қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Қызыл, Сары, Жасыл", "is_correct": True},
                    {"text": "Көк, Ақ, Қызыл", "is_correct": False},
                    {"text": "Жасыл, Күлгін, Қара", "is_correct": False},
                    {"text": "Тек Қызыл", "is_correct": False}
                ]
            }
        ],
        "ШИМ порттар": [
            {
                "text": "ШИМ (PWM) сигналдары Arduino-ның қандай пиндерінде қолжетімді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "~ (тильда) белгісі бар пиндерде (3, 5, 6, 9, 10, 11)", "is_correct": True},
                    {"text": "Барлық пиндерде", "is_correct": False},
                    {"text": "Тек аналогтық пиндерде (A0-A5)", "is_correct": False},
                    {"text": "Тек 13-пинде", "is_correct": False}
                ]
            },
            {
                "text": "analogWrite(pin, value) функциясындағы value мәні қандай аралықта болуы керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "0-ден 255-ке дейін", "is_correct": True},
                    {"text": "0-ден 1023-ке дейін", "is_correct": False},
                    {"text": "0-ден 100-ге дейін", "is_correct": False},
                    {"text": "-128-ден 127-ге дейін", "is_correct": False}
                ]
            }
        ],
        "RGB жарық диоды": [
            {
                "text": "RGB жарық диоды қандай түстерден тұрады?",
                "type": "question_type_OPEN",
                "correct_answer": "Red (Қызыл), Green (Жасыл), Blue (Көк)."
            },
            {
                "text": "RGB диодының жалпы (common) аяғы қайда қосылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "GND-ге (ортақ катод) немесе 5V-ке (ортақ анод)", "is_correct": True},
                    {"text": "Тек аналогтық пинге", "is_correct": False},
                    {"text": "Ешқайда қосылмайды", "is_correct": False},
                    {"text": "3.3V-ке", "is_correct": False}
                ]
            }
        ],
        "Red Green Blue": [
            {
                "text": "Барлық түстерді (R, G, B) 255 мәніне қойсақ, қандай түс шығады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Ақ", "is_correct": True},
                    {"text": "Қара", "is_correct": False},
                    {"text": "Сары", "is_correct": False},
                    {"text": "Қоңыр", "is_correct": False}
                ]
            },
            {
                "text": "Егер тек қызыл және көк түсті араластырсақ, қандай түс аламыз?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Күлгін (Magenta)", "is_correct": True},
                    {"text": "Сары", "is_correct": False},
                    {"text": "Көгілдір (Cyan)", "is_correct": False},
                    {"text": "Жасыл", "is_correct": False}
                ]
            }
        ],
        "Батырма - 1": [
            {
                "text": "Батырманың басылған күйін оқу үшін қандай функция қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "digitalRead()", "is_correct": True},
                    {"text": "analogRead()", "is_correct": False},
                    {"text": "digitalWrite()", "is_correct": False},
                    {"text": "analogWrite()", "is_correct": False}
                ]
            },
            {
                "text": "Батырманы қосқанда не үшін тартушы (pull-up/pull-down) резистор қажет?",
                "type": "question_type_OPEN",
                "correct_answer": "Сигналдың тұрақтылығын қамтамасыз ету және 'шуды' (жалған сигналдарды) болдырмау үшін."
            }
        ],
        "Батырма - 2": [
            {
                "text": "Батырманың 'дірілі' (bounce) дегеніміз не?",
                "type": "question_type_OPEN",
                "correct_answer": "Механикалық контактілер қосылған сәттегі сигналдың тұрақсыздығы, бір басуды бірнеше рет деп қабылдауға әкелуі мүмкін."
            },
            {
                "text": "Дірілді (bounce) жоюдың қарапайым бағдарламалық жолы қандай?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Қысқа уақытқа (мысалы 50мс) кідіріс (delay) қосу", "is_correct": True},
                    {"text": "Кернеуді арттыру", "is_correct": False},
                    {"text": "Резисторды алып тастау", "is_correct": False},
                    {"text": "Батырманы қаттырақ басу", "is_correct": False}
                ]
            }
        ],
        "Батырма - 3": [
            {
                "text": "INPUT_PULLUP режимі не істейді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Ишкі резисторды қосып, пинді 5V-ке тартады (инверсияланған логика)", "is_correct": True},
                    {"text": "Пинді жерге (GND) тартады", "is_correct": False},
                    {"text": "Пинді шығыс (OUTPUT) режиміне қосады", "is_correct": False},
                    {"text": "Токты күшейтеді", "is_correct": False}
                ]
            },
            {
                "text": "INPUT_PULLUP кезінде батырма басылғанда digitalRead қандай мән қайтарады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "LOW", "is_correct": True},
                    {"text": "HIGH", "is_correct": False},
                    {"text": "1023", "is_correct": False},
                    {"text": "0V", "is_correct": False} # Technically correct logically as 0, but usually LOW keyword is explicit
                ]
            }
        ],
        "Монитор портпен жұмыс": [
            {
                "text": "Serial Monitor терезесін ашқанда деректер дұрыс көрінуі үшін не маңызды?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Кодтағы және монитордағы жылдамдық (baud rate) бірдей болуы керек", "is_correct": True},
                    {"text": "Интернет байланысы болуы керек", "is_correct": False},
                    {"text": "Arduino тақтасының түсі көк болуы керек", "is_correct": False},
                    {"text": "Ештеңе маңызды емес", "is_correct": False}
                ]
            },
            {
                "text": "Serial.println() мен Serial.print() айырмашылығы неде?",
                "type": "question_type_OPEN",
                "correct_answer": "Serial.print() мәтінді сол жолға шығарады, ал Serial.println() соңынан жаңа жолға түсіреді."
            }
        ],
        "Пьезоэлемент": [
            {
                "text": "Arduino-да дыбыс шығару үшін қандай функция қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "tone()", "is_correct": True},
                    {"text": "sound()", "is_correct": False},
                    {"text": "play()", "is_correct": False},
                    {"text": "noise()", "is_correct": False}
                ]
            },
            {
                "text": "Активті және Пассивті буззердің айырмашылығы неде?",
                "type": "question_type_OPEN",
                "correct_answer": "Активті буззер тоқ бергенде өзі дыбыс шығарады, ал пассивті буззерге дыбыс шығару үшін жиілік (сигнал) беру керек."
            }
        ],
        "Потенциометр": [
            {
                "text": "Потенциометр Arduino-ның қандай пиндеріне қосылуы керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Аналогтық (A0-A5)", "is_correct": True},
                    {"text": "Сандық (0-13)", "is_correct": False},
                    {"text": "Тек 5V және GND", "is_correct": False},
                    {"text": "Тек PWM пиндерге", "is_correct": False}
                ]
            },
            {
                "text": "analogRead() функциясы қандай мәндер аралығын қайтарады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "0-1023", "is_correct": True},
                    {"text": "0-255", "is_correct": False},
                    {"text": "0-100", "is_correct": False},
                    {"text": "0-5000", "is_correct": False}
                ]
            }
        ],
        "RGB және Потенциометр": [
            {
                "text": "Потенциометрден алынған 0-1023 мәнін LED-ке беру үшін 0-255-ке қалай түрлендіреміз?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "map() функциясын қолдану арқылы", "is_correct": True},
                    {"text": "4-ке көбейту арқылы", "is_correct": False},
                    {"text": "100-ге бөлу арқылы", "is_correct": False},
                    {"text": "Түрлендірудің қажеті жоқ", "is_correct": False}
                ]
            },
            {
                "text": "Бұл жобада неше потенциометр қолданылды?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "3 (әр түске біреуден)", "is_correct": True},
                    {"text": "1 (барлығы үшін)", "is_correct": False},
                    {"text": "2 (тек қызыл мен көк үшін)", "is_correct": False},
                    {"text": "0", "is_correct": False}
                ]
            }
        ],
        "Фоторезистор": [
            {
                "text": "Фоторезистордың кедергісі неге байланысты өзгереді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Түскен жарықтың мөлшеріне", "is_correct": True},
                    {"text": "Ауа температурасына", "is_correct": False},
                    {"text": "Дыбыс деңгейіне", "is_correct": False},
                    {"text": "Уақытқа", "is_correct": False}
                ]
            },
            {
                "text": "Фоторезисторды оқу үшін қандай схема қолданылады?",
                "type": "question_type_OPEN",
                "correct_answer": "Кернеу бөлгіш (Voltage Divider) схемасы: фоторезистор және тұрақты резистор тізбектей жалғанады."
            }
        ],
        "Переключатель(Ауыстырғыш)": [
            {
                "text": "Ауыстырғыштың (Slide Switch) батырмадан айырмашылығы неде?",
                "type": "question_type_OPEN",
                "correct_answer": "Ауыстырғыш өз күйін (қосулы/өшірулі) механикалық түрде сақтайды, ал батырма тек басылып тұрғанда ғана іске қосылады."
            },
            {
                "text": "Ауыстырғышты қосқанда қысқа тұйықталу болмауы үшін не істеу керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "5V пен GND-ті бір уақытта ауыстырғыш арқылы қоспау керек", "is_correct": True},
                    {"text": "Тек қалың сымдарды қолдану керек", "is_correct": False},
                    {"text": "Сымдарды скотчпен орау керек", "is_correct": False},
                    {"text": "Ауыстырғышты қолданбау керек", "is_correct": False}
                ]
            }
        ],
        "Мультиметр және кедергі есептеу": [
            {
                "text": "Резисторлар тізбектей жалғанғанда, жалпы кедергі қалай өзгереді?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Артады (R = R1 + R2)", "is_correct": True},
                    {"text": "Азаяды", "is_correct": False},
                    {"text": "Өзгермейді", "is_correct": False},
                    {"text": "Нөлге тең болады", "is_correct": False}
                ]
            },
            {
                "text": "Мультиметрмен токты өлшеу үшін оны тізбекке қалай қосу керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Тізбектей (Series)", "is_correct": True},
                    {"text": "Параллель (Parallel)", "is_correct": False},
                    {"text": "Кез келген жолмен", "is_correct": False},
                    {"text": "Токты өлшеу мүмкін емес", "is_correct": False}
                ]
            }
        ],
        "Сервомотор": [
            {
                "text": "Сервомотордың қарапайым мотордан айырмашылығы неде?",
                "type": "question_type_OPEN",
                "correct_answer": "Сервомотор білікті нақты градусқа (бұрышқа) бұрып, сол позицияны ұстап тұра алады."
            },
            {
                "text": "Arduino-да сервомоторды басқару үшін қандай кітапхана қолданылады?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Servo.h", "is_correct": True},
                    {"text": "Motor.h", "is_correct": False},
                    {"text": "Stepper.h", "is_correct": False},
                    {"text": "Robot.h", "is_correct": False}
                ]
            }
        ],
        "Бірнеше сервомоторды басқару": [
            {
                "text": "Бірнеше сервомотор қолданғанда неге сыртқы қуат көзі қажет?",
                "type": "question_type_OPEN",
                "correct_answer": "Сервомоторлар көп ток тұтынады, Arduino-ның кірістірілген реттегіші қызып кетпеуі немесе кернеудің тұрақсыздығын болдырмау үшін."
            },
            {
                "text": "Сыртқы қуат көзін қосқанда нені ұмытпау керек?",
                "type": "question_type_MCQ",
                "choices": [
                    {"text": "Барлық GND (Жер) сымдарын біріктіруді", "is_correct": True},
                    {"text": "Барлық 5V сымдарын біріктіруді", "is_correct": False},
                    {"text": "Батарейканы теріс қосуды", "is_correct": False},
                    {"text": "Кернеуді 12V-қа көтеруді", "is_correct": False}
                ]
            }
        ]
    }
    
    # Compatibility mapping for QuestionType
    # Check if QuestionType is defined in choices as tuple (value, label) or just value
    try:
        if hasattr(QuestionType, 'MULTIPLE_CHOICE'):
            mcq_value = QuestionType.MULTIPLE_CHOICE
            open_value = QuestionType.OPEN_ENDED
        else:
            # Fallback values if enum is different
            mcq_value = 'MCQ'
            open_value = 'OPEN'
    except:
         mcq_value = 'MCQ'
         open_value = 'OPEN'

    # If we have predefined questions for this subject, use them
    if subject in realistic_questions and realistic_questions[subject]:
        # Use up to num_questions questions from our predefined set
        available_questions = realistic_questions[subject][:num_questions]
        
        for i, q_data in enumerate(available_questions, 1):
            # Fix type mapping
            q_type = mcq_value if q_data["type"] == "question_type_MCQ" else open_value

            question = {
                "id": f"q{i}",
                "text": q_data["text"],
                "type": q_type,
                "points": random.choice([1, 2, 3]),
                "order": i
            }
            
            # Add choices for multiple choice questions
            if q_data["type"] == "question_type_MCQ":
                choices = []
                correct_index = None
                
                for j, choice in enumerate(q_data["choices"], 1):
                    choices.append({
                        "id": f"q{i}_c{j}",
                        "text": choice["text"],
                        "is_correct": choice["is_correct"]
                    })
                    if choice["is_correct"]:
                        correct_index = j
                
                question["choices"] = choices
            
            # Add correct answer for open-ended questions
            if q_data["type"] == "question_type_OPEN":
                question["correct_answer"] = q_data["correct_answer"]
            
            questions.append(question)
    else:
        # Fallback to general robotics questions if no specific ones exist
        for i in range(1, num_questions + 1):
            # Alternate between multiple choice and open-ended questions
            is_mcq = (i % 2 == 0)
            question_type = mcq_value if is_mcq else open_value
            
            if is_mcq:
                question_text = f"{subject} тақырыбы бойынша дұрыс тұжырымды табыңыз."
            else:
                question_text = f"{subject} жұмыс істеу принципін түсіндіріңіз."
            
            question = {
                "id": f"q{i}",
                "text": question_text,
                "type": question_type,
                "points": random.choice([1, 2, 3]),
                "order": i
            }
            
            # Add choices for multiple choice questions
            if is_mcq:
                choices = []
                correct_choice = random.randint(1, 4)
                
                for j in range(1, 5):
                    is_correct = (j == correct_choice)
                    choice_text = f"Мүмкін жауап {j}" + (" (Дұрыс)" if is_correct else "")
                    
                    choices.append({
                        "id": f"q{i}_c{j}",
                        "text": choice_text,
                        "is_correct": is_correct
                    })
                
                question["choices"] = choices
            else:
                # Add default correct answer for open-ended questions
                question["correct_answer"] = f"Бұл тақырып робототехникада маңызды рөл атқарады. Негізгі принциптерді түсіну қажет."
            
            questions.append(question)
    
    return questions

def flush_database():
    """Flush database tables related to courses and questions."""
    print("Flushing existing course data...")
    try:
        # Delete data in reverse order of dependencies
        Choice.objects.all().delete()
        Question.objects.all().delete()
        Test.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        print("Database flushed successfully.")
    except Exception as e:
        print(f"Error flushing database: {e}")

def create_course_with_lessons():
    """Create a course and add lessons to it with detailed quiz data including correct answers."""
    # Create the course
    course, created = Course.objects.get_or_create(
        name="Робототехника негіздері",
        defaults={
            'description': "Бұл курс Arduino платформасы арқылы робототехника және электроника негіздерін үйретеді. Тинкеркад симуляторынан бастап, нақты схемалар құрастыруға дейін қамтиды."
        }
    )
    
    if created:
        print(f"Created new course: {course.name}")
    else:
        print(f"Using existing course: {course.name}")
        # Update description if it exists
        course.description = "Бұл курс Arduino платформасы арқылы робототехника және электроника негіздерін үйретеді. Тинкеркад симуляторынан бастап, нақты схемалар құрастыруға дейін қамтиды."
        course.save()
    
    # Define the lessons data with detailed Markdown content
    lessons_data = [
        {
            "title": "Тинкеркадпен танысу",
            "description": "Tinkercad онлайн платформасымен танысу.",
            "content": """# Tinkercad-қа кіріспе

## Tinkercad деген не?
Tinkercad - бұл 3D модельдеуге, электрониканы схемалауға және бағдарламалауға арналған қарапайым, тегін онлайн қосымша. Ол Autodesk компаниясымен жасалған және жаңадан бастаушылар үшін өте қолайлы.

## Негізгі мүмкіндіктері:
*   **3D Design**: Қарапайым фигуралардан күрделі 3D модельдер құру.
*   **Circuits**: Arduino және басқа микроконтроллерлер мен электронды компоненттерді жалғап, симуляция жасау.
*   **Codeblocks**: Блоктық кодтау арқылы 3D объектілерді жасау.

## Жұмысты бастау:
1.  [tinkercad.com](https://www.tinkercad.com) сайтына кіріңіз.
2.  Тіркеліңіз немесе Google аккаунты арқылы кіріңіз.
3.  "Create new" батырмасын басып, "Circuit" таңдаңыз.

## Интерфейспен танысу:
*   Оң жақта: Компоненттер кітапханасы (Резистор, LED, Arduino, т.б.).
*   Ортада: Жұмыс алаңы.
*   Жоғарыда: Код терезесі (Code), Симуляцияны бастау (Start Simulation).

Бұл сабақта біз Tinkercad ортасында алғашқы қарапайым схемамызды жинап көреміз.""",
            "video_url": "https://youtube.com/embed/3cuOYAf7qFg",
            "hours": 1,
            "references": "Tinkercad.com"
        },
        {
            "title": "Ардуино және Макеталық тақша",
            "description": "Arduino микроконтроллері және Breadboard.",
            "content": """# Arduino және Макеталық тақша (Breadboard)

## Arduino UNO
Arduino - бұл электронды құрылғыларды жасауға арналған ашық платформа. Ол аппараттық (плата) және бағдарламалық (Arduino IDE) бөліктерден тұрады.

**Arduino UNO құрылымы:**
*   **Микроконтроллер**: ATmega328P - тақшаның "миы".
*   **Сандық пиндер (Digital Pins)**: 0-13 (сигналдарды қабылдау және беру).
*   **Аналогтық пиндер (Analog Pins)**: A0-A5 (аналогтық датчиктер үшін).
*   **Қуат көзі (Power)**: 5V, 3.3V, GND (Жер).
*   **USB порт**: Компьютерге қосу және код жүктеу үшін.

## Макеталық тақша (Breadboard)
Breadboard - схемаларды дәнекерлеусіз (soldering) уақытша немесе прототип ретінде жинауға арналған құрылғы.

**Құрылымы:**
*   **Орталық бөлік**: Компоненттерді орнатуға арналған жолдар. Әр жол (5 нүкте) өзара электрлік байланысқан.
*   **Бүйірлік жолдар (+ және -)**: Қуат көзін таратуға арналған ұзын жолдар. Әдетте қызыл (+) және көк (-) сызықтармен белгіленеді.

**Маңызды ереже**: Ешқашан "+" пен "-"-ты тікелей қоспаңыз (қысқа тұйықталу)!""",
            "video_url": "https://youtube.com/embed/HtqlMkYpeIM",
            "hours": 1,
            "references": "Arduino.cc"
        },
        {
            "title": "Жарық диоды",
            "description": "Жарық диодының (LED) жұмысы.",
            "content": """# Жарық диоды (LED)

## Анықтама
Жарық диоды (Light Emitting Diode - LED) - электр тогы өткен кезде жарық шығаратын жартылай өткізгіш құрылғы.

## Полярлық
LED-тің екі аяқшасы бар және оларды дұрыс қосу маңызды:
1.  **Анод (+)**: Ұзын аяқша. Оң қуат көзіне жалғанады.
2.  **Катод (-)**: Қысқа аяқша. Жерге (GND) жалғанады.

## Резистордың маңызы
Жарық диодын Arduino-ға немесе батарейкаға тікелей қосуға **болмайды**. Ток тым көп өтіп, диод күйіп кетуі мүмкін.
Сондықтан, тізбектей **резистор (кедергі)** қосу керек.

**Әдеттегі номиналдар:**
*   220 Ом (Ом)
*   330 Ом
*   1 кОм (жарығырақ әлсіздеу болады)

## Қосу схемасы
`Arduino Pin 13` -> `Резистор (220 Ом)` -> `LED Анод (+)` -> `LED Катод (-)` -> `Arduino GND`.""",
            "video_url": "https://youtube.com/embed/iXp6sVDUbzs",
            "hours": 1,
            "references": "Электроника негіздері кітабы"
        },
        {
            "title": "Алғашқы бағдарлама",
            "description": "Arduino IDE және 'Blink'.",
            "content": """# Алғашқы бағдарлама: Blink

## Arduino IDE
Код жазуға арналған орта. Бағдарлама құрылымы екі негізгі функциядан тұрады:

```cpp
void setup() {
  // Мұндағы код бір рет орындалады (баптаулар)
  pinMode(13, OUTPUT); // 13-пин шығыс ретінде белгіленеді
}

void loop() {
  // Мұндағы код шексіз қайталанады
  digitalWrite(13, HIGH); // Жарықты қосу (5V беру)
  delay(1000);            // 1000 миллисекунд (1 секунд) күту
  digitalWrite(13, LOW);  // Жарықты өшіру (0V беру)
  delay(1000);            // 1 секунд күту
}
```

## Функциялар:
*   `pinMode(pin, mode)`: Пиннің режимін орнатады (INPUT немесе OUTPUT).
*   `digitalWrite(pin, value)`: Пиге кернеу береді (HIGH - қосу, LOW - өшіру).
*   `delay(ms)`: Бағдарламаның жұмысын көрсетілген уақытқа (миллисекунд) кідіртеді.

Бұл бағдарлама Arduino тақтасындағы кірістірілген жарық диодын (L) 1 секунд сайын жыпылықтатады.""",
            "video_url": "https://youtube.com/embed/No1k-OhLveI",
            "hours": 1,
            "references": "Arduino Language Reference"
        },
        {
            "title": "Бағдаршам",
            "description": "Үш түсті бағдаршам макетін жасау.",
            "content": """# Жоба: Бағдаршам

## Мақсаты
Үш жарық диодын (Қызыл, Сары, Жасыл) пайдаланып, жол қиылысындағы бағдаршамның жұмысын имитациялау.

## Қажетті құралдар:
*   Arduino UNO
*   Breadboard
*   3 x Жарық диоды (Қызыл, Сары, Жасыл)
*   3 x Резистор (220 Ом)
*   Сымдар

## Схема
1.  Қызыл LED -> Pin 13
2.  Сары LED -> Pin 12
3.  Жасыл LED -> Pin 11
4.  Барлық LED-тердің катодтары (-) резистор арқылы GND-ге қосылады.

## Алгоритм
1.  **Қызыл**: Қосулы (5 секунд), кейін өшеді.
2.  **Сары**: Қосулы (2 секунд), кейін өшеді.
3.  **Жасыл**: Қосулы (5 секунд), кейін жыпылықтайды (3 рет), сосын өшеді.
4.  Цикл қайтадан басталады.

Бұл тапсырма `digitalWrite` және `delay` функцияларын бекітуге өте жақсы.""",
            "video_url": "https://youtube.com/embed/A4u-S9kALFQ",
            "hours": 1,
            "references": ""
        },
        {
            "title": "ШИМ порттар",
            "description": "Pulse Width Modulation (PWM).",
            "content": """# ШИМ (PWM) Порттар

## ШИМ деген не?
ШИМ (Pulse Width Modulation - Импульстік ендік модуляция) - бұл сандық сигналды аналогтық сигналға ұқсатып шығару әдісі.
Сандық сигнал тек `0` (0V) немесе `1` (5V) бола алады. Алайда, ШИМ арқылы біз "орташа" кернеуді имитациялай аламыз.

## Қалай жұмыс істейді?
Сигнал өте жылдам жиілікте қосылып-өшеді. Қосулы тұрған уақыттың жалпы уақытқа қатынасы **Duty Cycle** деп аталады.
*   50% Duty Cycle = 2.5V (орташа) -> Жарық диоды жартылай жарықтықпен жанады.
*   10% Duty Cycle = 0.5V (орташа) -> Өте әлсіз жанады.
*   100% Duty Cycle = 5V -> Толық жарықтық.

## Arduino-дағы ШИМ
Arduino UNO-да ШИМ пиндері `~` белгісімен (тильда) белгіленген: 3, 5, 6, 9, 10, 11.

## Функция
`analogWrite(pin, value)`
*   `value`: 0-ден 255-ке дейінгі сан.
    *   0: Толық өшіру (0V).
    *   127: ~50% (2.5V).
    *   255: Толық қосу (5V).

Бұл әдіс жарық диодының жарықтығын («fading») немесе мотордың жылдамдығын басқару үшін қолданылады.""",
            "video_url": "https://youtube.com/embed/D_iXFwyXFrc",
            "hours": 1,
            "references": ""
        },
        {
            "title": "RGB жарық диоды",
            "description": "RGB түстерін түсіну.",
            "content": """# RGB Жарық диоды

## Құрылымы
RGB (Red, Green, Blue) жарық диоды бір корпуста үш түрлі түсті (қызыл, жасыл, көк) диодты біріктіреді. Оларды араластыру арқылы кез келген түсті алуға болады.

RGB диодтарының 4 аяғы бар:
1.  **Red (R)**: Қызылға жауап береді.
2.  **Ground (GND) / Common Cathode**: Ортақ минус.
3.  **Blue (B)**: Көкке жауап береді.
4.  **Green (G)**: Жасылға жауап береді.

*Ескерту: "Common Anode" (ортақ плюс) түрлері де болады, онда ортақ аяқ 5V-қа қосылады.*

## Қосу
Әр түстің (R, G, B) аяғына жеке резистор (220 Ом) қажет.
Әр түсті бөлек басқару үшін оларды ШИМ (PWM) пиндеріне қосқан дұрыс (мысалы: 9, 10, 11).

Мысалы, күлгін түсті алу үшін:
*   Қызыл: 100% қосамыз.
*   Көк: 100% қосамыз.
*   Жасыл: 0% (өшіреміз).""",
            "video_url": "https://youtube.com/embed/xAcTnSTkHsM",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Red Green Blue",
            "description": "RGB түстерін кодтау.",
            "content": """# Red Green Blue: Түстерді кодтау

## Түс кодтары
`analogWrite()` көмегімен түстерді араластыру.
Түс мәндері 0-255 аралығындағы (RGB Color Model).

### Негізгі түстер:
*   **Қызыл**: (255, 0, 0)
*   **Жасыл**: (0, 255, 0)
*   **Көк**: (0, 0, 255)

### Аралас түстер:
*   **Сары**: Қызыл + Жасыл (255, 255, 0)
*   **Көгілдір (Cyan)**: Жасыл + Көк (0, 255, 255)
*   **Күлгін (Magenta)**: Қызыл + Көк (255, 0, 255)
*   **Ақ**: Барлығы қосулы (255, 255, 255)
*   **Қызғылт сары**: (255, 165, 0)

## Практикалық тапсырма
Функция жазу:
```cpp
void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
```
Осы функцияны `loop()` ішінде шақырып, бағдаршам секілді түстерді бірқалыпты ауыстыруға болады.""",
            "video_url": "https://youtube.com/embed/ZhIh9RUNVSw",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Батырма - 1",
            "description": "Батырма (Button) және Digital Read.",
            "content": """# Батырмалармен жұмыс (1-бөлім)

## Тактильді батырма (Tactile Push Button)
Батырма - ең қарапайым енгізу құрылғысы. Басылған кезде тізбекті тұйықтайды, жібергенде ажыратады.

## Қосу схемасы
Батырма Arduino-ға қосылғанда, оның мәнін дұрыс оқу үшін **тартушы резистор (pull-down немесе pull-up resistor)** қажет.
Әйтпесе, батырма басылмаған кезде пинде "шу" (белгісіз сигнал) болады.

**Pull-down схемасы:**
1.  Батырманың бір аяғы: 5V.
2.  Батырманың екінші аяғы: Цифрлық пинге (мысалы 2) ЖӘНЕ 10кОм резистор арқылы GND-ге.
*   Басылмағанда: Пин GND-ге резистор арқылы қосылады -> LOW (0V).
*   Басылғанда: Пин тікелей 5V-ке қосылады -> HIGH (5V).

## Кодтау: `digitalRead()`
```cpp
const int buttonPin = 2;
const int ledPin = 13;
int buttonState = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin); // Батырма күйін оқу
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH); // Егер басылса, LED-ті қос
  } else {
    digitalWrite(ledPin, LOW);  // Әйтпесе, өшір
  }
}
```""",
            "video_url": "https://youtube.com/embed/0ihhorM7hOE",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Батырма - 2",
            "description": "Батырманың дірілін жою (Debounce).",
            "content": """# Батырмалармен жұмыс (2-бөлім): Debounce

## Мәселе: Байланыс дірілі (Bouncing)
Батырма - механикалық құрылғы. Оны басқан кезде, металл контактілер бірден тұрақты қосылмайды. Олар микросекундтар бойы дірілдеп, процессорға "қосылды-өшті-қосылды-өшті" деген көптеген жалған сигналдар жібереді.
Нәтижесінде, бір рет басқанның өзінде Arduino оны бірнеше рет басылды деп қабылдауы мүмкін.

## Шешімі: Бағдарламалық Debounce
Сигнал тұрақтанғанын күту керек.
Қарапайым шешім - кішкене кідіріс қосу:

```cpp
if (digitalRead(buttonPin) == HIGH) {
  delay(50); // 50 миллисекунд күтіп, дірілді өткізіп жібереміз
  if (digitalRead(buttonPin) == HIGH) {
    // Егер әлі де басулы болса, онда бұл нақты сигнал
  }
}
```

## Батырма режимі: Toggle (Ауыстырып қосқыш)
Батырманы әр басқан сайын жарық күйін ауыстыру (қосу -> өшіру -> қосу).
Бұл үшін айнымалы (flag) қолданамыз:
```cpp
bool ledState = false;
// ... басу анықталғанда:
ledState = !ledState; // Күйді керісінше өзгерту
digitalWrite(ledPin, ledState ? HIGH : LOW);
```""",
            "video_url": "https://youtube.com/embed/u79UZ652aGI",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Батырма - 3",
            "description": "INPUT_PULLUP режимі.",
            "content": """# Батырмалармен жұмыс (3-бөлім): INPUT_PULLUP

## Кірістірілген резисторлар
Сыртқы резисторларды қолданбас үшін, Arduino микроконтроллерінің ішіндегі **INPUT_PULLUP** режимін қолдануға болады. Бұл режим пинді ішкі 20кОм резистор арқылы 5V-ке қосады.

## Ерекшелігі: Инверсияланған логика
*   **Басылмағанда:** Пин 5V-ке тартылып тұр -> Оқылатын мән **HIGH**.
*   **Басылғанда:** Батырма пинді GND-ге қосады -> Оқылатын мән **LOW**.

## Схема
Батырманың бір аяғы -> Пинге.
Екінші аяғы -> GND-ге.
(Сыртқы резистор қажет емес).

## Код
```cpp
void setup() {
  pinMode(2, INPUT_PULLUP); // 2-пинді pull-up режимінде қосу
}

void loop() {
  int sensorVal = digitalRead(2);
  if (sensorVal == LOW) { // Басылғанда LOW болады!
    // Әрекет орындау
  }
}
```
Бұл схема жинауды жеңілдетеді және компоненттер санын азайтады.""",
            "video_url": "https://youtube.com/embed/0f8VJi5cUfA",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Монитор портпен жұмыс",
            "description": "Serial Monitor және Debugging.",
            "content": """# Serial Port (Сериялық порт)

## Serial Monitor
Бұл - Arduino мен Компьютер арасындағы "чат". Ол программаны жөндеуге (debug) және датчиктердің мәнін көруге өте қажет.

## Негізгі командалар:
1.  **`Serial.begin(9600);`**: `setup()` бөлімінде байланысты бастау. 9600 - бұл жылдамдық (baud rate).
2.  **`Serial.print("Text");`**: Мәтінді бір жолға шығару.
3.  **`Serial.println("Text");`**: Мәтінді шығарып, жаңа жолға түсу.
4.  **`Serial.available()`**: Порттан деректер келгенін тексеру.
5.  **`Serial.read()`**: Деректерді оқу.

## Мысалы:
```cpp
void setup() {
  Serial.begin(9600); 
}

void loop() {
  Serial.println("Hello Arduino!");
  delay(1000);
}
```
Нәтижені көру үшін Arduino IDE-де жоғарғы оң жақтағы лупа белгішесін (Serial Monitor) басу керек.""",
            "video_url": "https://youtube.com/embed/56VhGWIfMNA",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Пьезоэлемент",
            "description": "Buzzer және дыбыс шығару.",
            "content": """# Пьезоэлемент (Piezo Buzzer)

## Құрылымы
Пьезоэлемент кернеу бергенде дірілдеп, дыбыс шығаратын құрылғы.

## Түрлері
1.  **Активті**: Ток бергенде бірден дайын дыбыс ("пип") шығарады.
2.  **Пассивті**: Дыбыс шығару үшін жиілік (тональность) беру керек. Музыка ойнай алады.

## Функция: `tone()`
Пассивті буззермен ноталарды ойнату үшін:
`tone(pin, frequency, duration)`
*   `pin`: Қосылған пин нөмірі.
*   `frequency`: Дыбыс жиілігі Герцпен (мысалы, 440 Гц - "Ля" нотасы).
*   `duration`: Ұзақтығы (миллисекунд).

Дыбысты тоқтату үшін: `noTone(pin)`.

## Қосу
Плюс аяғын цифрлық пинге, минус аяғын GND-ге қосамыз.

## Мысал (Сирена):
```cpp
tone(8, 440);
delay(500);
tone(8, 880);
delay(500);
```""",
            "video_url": "https://youtube.com/embed/dSu6fXtFtPQ",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Потенциометр",
            "description": "Аналогтық сигнал және айнымалы резистор.",
            "content": """# Потенциометр

## Анықтама
Потенциометр - кедергісін қолмен өзгертуге болатын реттелетін резистор.
Оның 3 аяғы бар:
1.  Шеткі аяғы: 5V.
2.  Шеткі аяғы: GND.
3.  Ортаңғы аяғы: Сигнал (Аналогтық пинге барады).

Бұрау арқылы ортаңғы аяқтағы кернеуді 0V-тен 5V-ке дейін бірқалыпты өзгертеміз.

## Аналогтық-Сандық Түрлендіргіш (ADC)
Arduino-ның аналогтық пиндері (A0-A5) кернеуді 0-ден 1023-ке дейінгі сандық мәнге айналдырады.
*   0V -> 0
*   5V -> 1023

## Функция: `analogRead()`
```cpp
int sensorValue = analogRead(A0);
// sensorValue 0 және 1023 арасында болады
```

Мұны жарық диодының жарықтығын басқару үшін (0-255) қолдануға болады. Ол үшін `map()` функциясы пайдалы:
`int brightness = map(sensorValue, 0, 1023, 0, 255);`""",
            "video_url": "https://youtube.com/embed/HnI9wdQPBto",
            "hours": 1,
            "references": ""
        },
        {
            "title": "RGB және Потенциометр",
            "description": "Түсті қолмен басқару.",
            "content": """# Жоба: RGB және Потенциометр

## Тапсырма
Үш потенциометр арқылы RGB жарық диодының үш түсін (Қызыл, Жасыл, Көк) жеке-жеке басқару. Бұл "Color Mixer" (Түс араластырғыш) деп аталады.

## Құрамдастар:
*   1 x RGB LED.
*   3 x Резистор (220 Ом).
*   3 x Потенциометр.

## Схема:
*   RGB пиндері -> PWM пиндерге (9, 10, 11).
*   Потенциометрлердің ортаңғы аяқтары -> A0, A1, A2 пиндеріне.

## Логика:
```cpp
// 1. Оқимыз (0-1023)
int rVal = analogRead(A0);
int gVal = analogRead(A1);
int bVal = analogRead(A2);

// 2. Түрлендіреміз (0-255)
rVal = map(rVal, 0, 1023, 0, 255);
gVal = map(gVal, 0, 1023, 0, 255);
bVal = map(bVal, 0, 1023, 0, 255);

// 3. Жазамыз
analogWrite(redPin, rVal);
analogWrite(greenPin, gVal);
analogWrite(bluePin, bVal);
```
Осылайша кез келген түсті қолмен шығарып алуға болады.""",
            "video_url": "https://youtube.com/embed/iprvzqVjLo8",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Фоторезистор",
            "description": "Жарық датчигі.",
            "content": """# Фоторезистор (LDR)

## Жұмыс принципі
Фоторезистор (Light Dependent Resistor) - жарық түскенде кедергісін өзгертетін компонент.
*   Қараңғыда: Кедергі өте жоғары (МОм).
*   Жарықта: Кедергі төмендейді (100 Ом - бірнеше кОм).

## Кернеу бөлгіш (Voltage Divider)
Фоторезистордың кедергісі өзгергенін Arduino оқуы үшін, оны тұрақты резистормен (мысалы 10 кОм) тізбектей жалғап, "кернеу бөлгіш" схемасын жасаймыз.
Ортаңғы нүктеден (екі резистордың түйіскен жерінен) аналогтық сигнал (A0) аламыз.

## Жоба: "Түнгі шам"
Бөлме қараңғыланғанда автоматты түрде жанатын шам жасау.

```cpp
int light = analogRead(A0);
if (light < 500) { // Егер қараңғы болса (шекті мәнді тәжірибе арқылы табамыз)
  digitalWrite(ledPin, HIGH);
} else {
  digitalWrite(ledPin, LOW);
}
```""",
            "video_url": "https://youtube.com/embed/m0PWyijtOOc",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Переключатель(Ауыстырғыш)",
            "description": "Слайд ауыстырғыш (Slide Switch).",
            "content": """# Ауыстырғыш (Slide Switch)

## Құрылымы
Бұл батырмаға ұқсас, бірақ басып тұруды қажет етпейді. Оның екі тұрақты күйі бар (Қосулы/Өшірулі).
Әдетте 3 аяғы бар:
1.  Шеткі 1.
2.  Ортақ (Common).
3.  Шеткі 2.

## Қосу
Көбінесе екі шеткі аяғын 5V пен GND-ге, ал ортаңғы аяғын Arduino-ның цифрлық пиніне қосады.
Бұл кезде **қысқа тұйықталу болмауы үшін** абай болу керек!

Қауіпсіз әдіс:
*   Бір шеткі аяқ бос қалады.
*   Ортаңғы аяқ -> Пинге.
*   Шеткі аяқ -> GND.
*   Arduino-да `INPUT_PULLUP` режимін қолданамыз.
    *   Ауыстырғыш қосулы (GND-ге тиіп тұр) -> LOW.
    *   Ауыстырғыш ашық -> HIGH.

Бұл құрылғыны режимдерді ауыстыру үшін (мысалы, роботтың "Автономды" және "Басқару" режимдері арасында) қолдануға болады.""",
            "video_url": "https://youtube.com/embed/t8tysWNP93M",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Мультиметр және кедергі есептеу",
            "description": "Электроника құралдары.",
            "content": """# Мультиметрмен жұмыс

## Мультиметр деген не?
Бұл электроншының басты құралы. Ол мыналарды өлшей алады:
1.  **Вольтметр (V)**: Кернеуді өлшеу (Параллель қосылады).
2.  **Амперметр (A)**: Токты өлшеу (Тізбектей қосылады - тізбекті үзу керек!).
3.  **Омметр (Ω)**: Кедергіні өлшеу (Токсыз кезде өлшеу керек).
4.  **Прозвонка**: Тізбектің тұтастығын тексеру (сым үзілмеген бе?).

## Кедергіні есептеу
Резисторларды қосқанда жалпы кедергі қалай өзгереді?

1.  **Тізбектей қосу (Series)**:
    `R_total = R1 + R2 + ...`
    Кедергі артады.

2.  **Параллель қосу (Parallel)**:
    `1 / R_total = 1/R1 + 1/R2 + ...`
    Кедергі азаяды.

Тәжірибеде мультиметрмен осы заңдылықтарды тексеріп көру керек.""",
            "video_url": "https://youtube.com/embed/Qu0m6c3lpzg",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Сервомотор",
            "description": "Серво жетегімен жұмыс (Servo).",
            "content": """# Сервомотор (Servo)

## Ерекшелігі
Кәдімгі DC моторлар үздіксіз айналады. Ал Сервомотор **нақты бұрышқа** (әдетте 0-ден 180 градусқа дейін) бұрылып, сол позицияны ұстап тұра алады.
Роботтардың қолдары, буындары үшін таптырмас құрал.

## Қосылуы (3 сым)
1.  **Қызыл**: 5V.
2.  **Қоңыр/Қара**: GND.
3.  **Сары/Оранж**: Сигнал (PWM пинге, мысалы ~9).

## Servo кітапханасы
Arduino-мен басқару өте оңай:

```cpp
#include <Servo.h> // Кітапхананы қосу

Servo myservo; // Объект құру

void setup() {
  myservo.attach(9); // 9-пинге жалғау
}

void loop() {
  myservo.write(0);   // 0 градусқа бұрылу
  delay(1000);
  myservo.write(90);  // 90 градусқа
  delay(1000);
  myservo.write(180); // 180 градусқа
  delay(1000);
}
```""",
            "video_url": "https://youtube.com/embed/lKKuWJBjIEM",
            "hours": 1,
            "references": ""
        },
        {
            "title": "Бірнеше сервомоторды басқару",
            "description": "Күрделі механизмдер.",
            "content": """# Бірнеше Сервомоторды басқару

## Қолданылуы
Робот-манипулятор (Robot Arm) немесе жүретін роботтар (Hexapod) жасағанда бірнеше сервомотор керек.

## Қосу
Әр серво жеке сигналдық пинге қосылады.
**МАҢЫЗДЫ**: Сервомоторлар көп ток тұтынады. Егер 2-ден көп серво қоссаңыз, Arduino-ның 5V қуаты жетпей қалуы мүмкін (Arduino қайта-қайта өшіп қалады).
Сондықтан, сервомоторларға **сыртқы қуат көзін** (батарейка блогы, 4xAA) қолдану керек.
*   Батарейканың (+) -> Серволардың (+) сымына.
*   Батарейканың (-) -> Серволардың (-) сымына ЖӘНЕ Arduino-ның GND пиніне (**GND біріктіру міндетті!**).

## Код
```cpp
Servo servo1;
Servo servo2;

void setup() {
  servo1.attach(9);
  servo2.attach(10);
}

void loop() {
  // Екеуін бірге басқару
  servo1.write(45);
  servo2.write(135);
}
```""",
            "video_url": "https://youtube.com/embed/A2FJfxTwK2k",
            "hours": 1,
            "references": ""
        }
    ]
    
    # Create lessons
    print(f"Creating {len(lessons_data)} lessons...")
    for i, data in enumerate(lessons_data, 1):
        defaults_dict = {
            'title': data['title'],
            'video_url': data['video_url'],
            'content': data.get('content', ''),
        }

        lesson, created = Lesson.objects.get_or_create(
            course=course,
            title=data['title'],
            defaults=defaults_dict
        )

        if not created:
            lesson.video_url = data['video_url']
            lesson.content = data.get('content', '')
            lesson.save()
            
        print(f"  Lesson {i}: {lesson.title}")
        
        # Create test for the lesson
        test, created = Test.objects.get_or_create(
            lesson=lesson,
            defaults={
                'title': f"Test: {lesson.title}",
                'description': f"Quiz for lesson {lesson.title}"
            }
        )
        
        # Determine number of questions (default to 3)
        num_questions = 3
        
        # Generate questions using the natural questions generator
        questions = create_quiz_questions(lesson.title, lesson.title, num_questions)
        
        # Create questions in database
        # First, remove existing questions to avoid duplicates/conflicts if re-running
        test.questions.all().delete()
        
        for q_data in questions:
            question = Question.objects.create(
                test=test,
                text=q_data["text"],
                question_type=q_data["type"],
                points=q_data["points"],
                order=q_data["order"],
                correct_answer=q_data.get("correct_answer", "")
            )
            
            # Create choices for multiple choice questions
            if "choices" in q_data:
                for c_data in q_data["choices"]:
                    Choice.objects.create(
                        question=question,
                        text=c_data["text"],
                        is_correct=c_data["is_correct"]
                    )

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1 and sys.argv[1] == '--flush':
            flush_database()
        
        create_course_with_lessons()
        print("Successfully populated robotics course.")
        
    except Exception as e:
        print(f"Error: {e}")
        # import traceback
        # traceback.print_exc()