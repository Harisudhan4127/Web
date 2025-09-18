from flask import Flask, request, jsonify, render_template
import difflib
from spellchecker import SpellChecker

app = Flask(__name__)

# -------------------- Q&A DATA --------------------

qa_data = [
        {
        "id": "Admission in collage.",
        "questions": [
            "admission in mvit clg",
            "admission in mit clg",
            "I want to put admission in mvit clg",
            "I want to put admission in mit clg",
            "I want to put admission for AIML course in your collage.",
            "I want to put admission for IOT course in your collage.",
            "I want to put admission for FT course in your collage.",
            "I want to put admission for RA course in your collage.",
            "I want to put admission for MECH course in your collage.",
            "I want to put admission for IT course in your collage.",
            "I want to put admission for CSE course in your collage.",
            "I want to put admission for ECE course in your collage.",
            "I want to put admission for EEE course in your collage.",
            "admission for EEE.",
            "admission"
        ],
        "answer": "https://forms.gle/rCcmmLxLe1waj3tJ8 <br> (you can put your admission by using this link)"
    },
    {
        "id": "AIML_STAFF",
        "questions": [
            "aiml mentors",
            "aiml professors",
            "aiml teachers",
            "aiml staff",
            "aiml faculty",
            "staff aiml"
        ],
        "answer": "1.Mr.R. RAJ BHARATH <br> https://i.ibb.co/vxWt071p/Screenshot-20250918-104230.jpg <br>"
        "2.Mrs.S.K SUGUNEDHAM <br> https://i.ibb.co/sS1sp64/Screenshot-20250917-100823.jpg <br>"
        "3.Mrs.S. CHITRA <br> https://i.ibb.co/JWHkZzyQ/Screenshot-20250917-100838.jpg <br>"
        "4.Mr.A. JAINULLABEEN <br> https://i.ibb.co/WvRywr5b/Screenshot-20250917-100856.jpg <br>"
        "5.Mrs.S. LAVANYA <br>https://i.ibb.co/C5D6Cwtc/Screenshot-20250917-100926.jpg  <br>"
        "6.Ms.V. DIANA <br> https://i.ibb.co/qLvDRTb8/Screenshot-20250917-101145.jpg  <br>"
        "7.Ms.K. REVATHI <br> https://i.ibb.co/vx96FNV9/Screenshot-20250917-101009.jpg  <br>"
        "8.Mrs.S. PRAVEENA <br> https://i.ibb.co/8D8TDKnR/Screenshot-20250917-101057.jpg  <br>"
        "9.Mrs.P. SUGANYA <br> https://i.ibb.co/7txkqXCt/Screenshot-20250917-101119.jpg  <br>"
        "10.Mr.R. RENGA NAYAGI <br> https://i.ibb.co/vxX4cYFX/Screenshot-20250917-101134.jpg  <br>"
        "They are the faculty of AIML in 2025-26. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "Bot name.",
        "questions": [
            "your name.",
            "what is your name.",
            "tell me your name.",
            "name"
        ],
        "answer": "My name is AK."
    },
    {
        "id": "bus_clg",
        "questions": [
            "mvit bus",
            "buses in mvit clg",
            "buses in mvit",
            "mvit bus routes",
            "mvit bus stops",
            "manakula vinayagar institute of technology buses",
            "mvit bus details",
            "clg bus details",
            "clg bus",
            "bus details"
        ],
        "answer": "img:/static/images/bus_fees.jpeg"
    },
    {
        "id": "bus image",
        "questions": [
            "mvit bus image",
            "buses images mvit clg",
            "buses pic in mvit",
            "mvit bus pics",
            "mvit bus pictures",
            "manakula vinayagar institute of technology bus image",
            "mvit bus pic",
            "clg bus photo",
            "clg photos"
        ],
        "answer": "img:/static/images/bus.jpeg"
    },
    {
        "id": "canteen",
        "questions": [
            "canteen food",
            "foods available in manakula vinayagar institute of technology",
            "food in collage canteen",
            "what are the food available in canteen",
            "ground floor canteen menu",
            "canteen menu"
        ],
        "answer": "img:/static/images/canteen.jpeg"
    },
    {
        "id": "clg_estabilsed",
        "questions": [
            "clg started details",
            "clg opening details",
            "when did the collage established"
        ],
        "answer": "manakula vinayager institute of technology was started at 2008 in madagadipet. and it was approved by AICTE. and also this institute was accredited by NAAC with 'A; grade and NBA."
    },
    {
        "id": "clg_information",
        "questions": [
            "mvit web page",
            "clg website",
            "clg web link",
            "mvit website",
            "mvit clg",
            "mit collage",
            "your clg website",
            "your clg web",
            "your collage website",
            "I want details about your collage",
            "I want details about my collage",
            "give some information about my collage",
            "give some information about your collage",
            "web"
        ],
        "answer": "https://mvit.edu.in/<br> (you can visit our clg website)"
    },
    {
        "id": "clg_location",
        "questions": [
            "give me the information were the clg is located",
            "mvit location",
            "mvit in map",
            "clg location in map",
            "clg location in google map",
            "clg map",
            "where did the collage located",
            "collage location link",
            "collage location"
        ],
        "answer": "Manakula vinayagar institute of technology was located in Madagadipet.<br>"
        " ( you can also use the given link to find the exact location of our collage) <br>"
        "https://maps.app.goo.gl/Z15uPr65jNhRfe117"
    },
    {
        "id": "computer_lab",
        "questions": [
            "cse lab",
            "manakula vinayagar institute of technology computer lab",
            "cs lab in mvit clg",
            "computer lab in mvit",
            "photo of computer lab",
            "images of cse lab",
            "copmuter lab"
        ],
        "answer": "img:/static/images/computer_lab.jpeg"
    },
    {
        "id": "courses in our clg",
        "questions": [
            "course in our clg",
            "what are the engineering courses offered in your collage.",
            "courses in mvit collage.",
            "courses in your clg.",
            "courses in your collage.",
            "what  are courses in your clg.",
            "what  are courses in your collage.",
            "deprtments",
            "departments in our clg",
            "what are the deparments are in mvit",
            "dept"
        ],
        "answer": "I have only information about engineering branch.<br>"
        " so the engineering courses offered by our collage in the year of 2025-26 are:<br>"
        "EEE,<br> ECE,<br> CSE,<br> IT,<br> MECH,<br> RA,<br> FT,<br> IOT,<br> AIML,<br>"
    },                                                                                      
    {
        "id": "Default Welcome Intent",
        "questions": [
            "just going to say hi",
            "heya",
            "hello hi",
            "hai",
            "hey there",
            "hi there",
            "greetings",
            "hey",
            "long time no see",
            "hello",
            "lovely day isn't it",
            "I greet you",
            "hello again",
            "hi",
            "hello there",
            "a good day"
        ],
        "answer": "Hello! How can I help you?"
    },
    {
        "id": "digital_library",
        "questions": [
            "internet library",
            "online library",
            "other library",
            "digital library in manakula vinayagar institute of technology , pondicheery",
            "digital library in mvit pondicheery",
            "digital library"
        ],
        "answer": "img:/static/images/digital_library.jpeg"
    },
    {
        "id": "eee_staff",
        "questions": [
            "Eee mentors",
            "EEE teachers",
            "eee professers",
            "eee staff",
            "eee faculty",
            "staff eee",
            "electrical and electronics communication staff"
        ],
        "answer": "1.Dr.C. SHANMUGASUNDARAM (HOD)<br> https://i.ibb.co/60s9xkNR/Screenshot-20250917-145828.jpg <br>"
        "2.Dr.K. SEDHURAMAN <br> https://i.ibb.co/RG6W9n11/Screenshot-20250917-145853.jpg <br>"
        "3.Mr.S. RAJKUMAR <br> https://i.ibb.co/0pjTrkXb/Screenshot-20250917-150009.jpg <br>"
        "4.Mr.N. AMARABALAN <br> https://i.ibb.co/WvXrzrt6/Screenshot-20250917-150040.jpg <br>"
        "5.Mr.D. BALAJI <br>  https://i.ibb.co/TqWKm0fw/Screenshot-20250917-150054.jpg <br>"
        "7.Mrs.R. UMAMAHESWARI <br> https://i.ibb.co/gbGjNmwB/Screenshot-20250917-150345.jpg <br>"
        "8.Mrs.S. SANTHALAKSHMY <br> https://i.ibb.co/GfRW5QVj/Screenshot-20250917-150318.jpg <br>"
        "9.Mrs.R. MUTHUNAGAI <br> https://i.ibb.co/kVfLT50v/Screenshot-20250917-150205.jpg  <br>"
        "10.Mrs.R. PRIYA <br> https://i.ibb.co/PsV4Mtf2/Screenshot-20250917-150306.jpg  <br>"
        "11.Mrs.J. VIJAYA RAGHAVAN <br> https://i.ibb.co/msvy6c9/Screenshot-20250917-150230.jpg <br>"
        "They are the faculty of EEE in 2025-26. <br> You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "ece_staff",
        "questions": [
            "Ec e mentors",
            "EcE teachers",
            "ece professers",
            "ECE staff",
            "ECE faculty",
            "staff ece",
            "EcE STAFF",
            "ec estaff",
            "ecestaff"
            "electronics and communication engineering staff"
        ],
        "answer":"1Dr.A.THENMOZHI	(PROFESSOR) <br>"
                 "2Dr.R.VALLI (PROFESSOR) <br>"
                 "3Dr.S.ARUNMOZHI  (PROFESSOR) <br>"
                 "4Dr.M.JAYEKUMAR	(PROFESSOR) <br>"
                 "5Dr.S.SEMMALAR (ASSOCIATE PROFESSOR) <br>"
                 "6Dr.R.SOFIA (ASSOCIATE PROFESSOR) <br>"
                 "7Dr.V.GOWTHAMI  (ASSOCIATE PROFESSOR) <br>"
                 "8Dr.S.VINOTH  (ASSOCIATE PROFESSOR) <br>"
                 "9Dr.M.SIVASINDHU  (ASSOCIATE PROFESSOR) <br>"
                 "10Mr.V.RAJESH  (ASSISTANT PROFESSOR) <br>"
                 "11Mr.K.KUMARAN  (ASSISTANT PROFESSOR) <br>"
                 "12Ms.K.ALAMELU  (ASSISTANT PROFESSOR) <br> They are the faculty of ECE in 2025-26."
    },
    {
        "id": "cse_staff",
        "questions": [
            "cse mentors",
            "CSE teachers",
            "Cse professers",
            "cse staff",
            "cse faculty",
            "staff cse",
            "cse STAFF",
            "computer science engineering staff"
        ],
        "answer":"1.Dr. S.Pariselvam (HOD) <br> https://i.ibb.co/qG387cc/Screenshot-20250918-075408.jpg <br>"
                 "2.Mrs.G.Sharmila <br> https://i.ibb.co/tpR3sT8X/IMG-20250918-113547.jpg <br>"
                 "3.Mr. R. Sathish Kumar <br> https://i.ibb.co/bM7Tnq40/Screenshot-20250918-075426.jpg <br>"
                 "4.Mrs. I. Varalakshmi <br> https://i.ibb.co/3YRJZXwM/Screenshot-20250918-075532.jpg <br>"
                 "5.Mrs. J. Jayapradha <br> https://i.ibb.co/s9WCngj3/Screenshot-20250918-113445.jpg <br>"
                 "6.Mr.A.Sankaran <br> https://i.ibb.co/Y7gknsqw/Screenshot-20250918-075557.jpg <br>"
                 "7Mrs. J. Jayapradha <br> https://i.ibb.co/s9WCngj3/Screenshot-20250918-113445.jpg <br>"
                 "8.Mrs. N. Kavitha <br> https://i.ibb.co/Y4BgzYPZ/Screenshot-20250918-113646.jpg <br>"
                 "9.Mrs. P. Suganya <br> https://i.ibb.co/bRGNYKtM/Screenshot-20250918-113657.jpg <br>"
                 " They are the faculty of CSE in 2025-26."
    },
    {
        "id": "it_staff",
        "questions": [
            "it mentors",
            "IT staff",
            "i t professers",
            "IT staff",
            "it faculty",
            "staff it",
            "it STAFF",
            "information technology staff"
        ],
        "answer": "1.Dr.P.Sivakumar (Professor) <br>"
                  "2.Dr.A. Meiappane (Professor) <br>"
                  "3.Mr. S. Uthayashangar (Assistant Professor) <br>"
                  "4.Ms. A. Punitha (Assistant Professor) <br>"
                  "5.Ms. J. Prabavadhi (Assistant Professor) <br>"
                  "6.Mr. K. Premkumar (Assistant Professor) <br>"
                  "7.	Mrs.L.Sankari (Assistant Professor) <br>"
                  "8.Mr.S.Shanmugasundaram (Assistant Professor) <br>"
                  "9.Ms.R.Dhamayanthi (Assistant Professor) <br>"
                  "10.Ms.V.Abirami(Assistant Professor) <br>"
                  "11.Mrs.D.Sudha (Assistant Professor) <br>"
                  "12.Mrs. G. Anuradha <br> They are the faculty of IT in 2025-26."
    },
    {
        "id": "fees for AIML",
        "questions": [
            "artificial intelligence and machine learning fees",
            "aiml fees",
            "fees for AIML.",
            "tell me the fees structure for AIML."
        ],
        "answer": "The fees structure for AIML  in 2025-26.for centac students is Rs:52,700 and for  management is Rs:81,500."
    },
    {
        "id": "fees for CSC.",
        "questions": [
            "computer science and engineering fees",
            "computer science fees",
            "cse fees",
            "fees for CSE.",
            "tell me the fees structure for CSE."
        ],
        "answer": "The fees structure for CSE in 2025-26.for centac students is Rs:62,700 and for management students is Rs:91,500"
    },
    {
        "id": "fees for ECE",
        "questions": [
            "electronics and communication engineering fees",
            "ece fees",
            "fess for ECE",
            "tell me the fees structure for ECE."
        ],
        "answer": "The fess structure for ECE in 2025-26.for centac students is Rs:62,700 and for management students is Rs:81,500."
    },
    {
        "id": "fees for FT",
        "questions": [
            "food technology fees",
            "ft fees",
            "fees for FT.",
            "tell me the fees structure for FT."
        ],
        "answer": "The fees structure for FT in 2025-26.for centac students is Rs:52,700 and for management students is Rs:71,500."
    },
    {
        "id": "fees for IOT",
        "questions": [
            "information of things fees",
            "iot fees",
            "fees for IOT.",
            "tell me the fees structure for IOT."
        ],
        "answer": "The fees structure IOT  for in 2025-26.for centac students is Rs:52,700 and for management students is Rs:81,500."
    },
    {
        "id": "fees for IT",
        "questions": [
            "information technology fees",
            "it fees",
            "fees for IT.",
            "tell me the fees structure for IT."
        ],
        "answer": "The fees structure for IT in 2025-26.for centac students is Rs:62,700 and for management students is Rs:91,500."
    },
    {
        "id": "fees for MECH",
        "questions": [
            "mechanical engineering fees",
            "mech fees",
            "fees for MECH.",
            "tell me the fees structure for MECH."
        ],
        "answer": "The fees structure for MECH in 2025-26.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "fees for RA",
        "questions": [
            "robotics and automation fees",
            "robotics fees",
            "fees for robotics",
            "fees for RA",
            "tell me the fees structure for RA."
        ],
        "answer": "The fees structure for RA in 2025-26.for centac students is Rs:52,700 and for management students is Rs:71,500."
    },
    {
        "id": "fess for EEE",
        "questions": [
            "electrical and electronic engineering fees",
            "eee fees",
            "fees for EEE.",
            "fees structure for EEE.",
            "tell me the fees structure for EEE."
        ],
        "answer": "The fess structure for EEE in 2025-26.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "FT_STAFF",
        "questions": [
            "FT professors",
            "ft techers",
            "ft mentors",
            "ft faculty",
            "f t staff"
        ],
        "answer": "1.Dr.D. Tiroutchelvame https://in.docworkspace.com/d/sICO4hYOQAsf5sLcG?sa=cl  <br>"
        "2.Dr.S. Aruna https://in.docworkspace.com/d/sIEy4hYOQAvv5sLcG?sa=cl  <br>"
        "3.Dr.S. Santhalakshmy https://in.docworkspace.com/d/sICe4hYOQAor6sLcG?sa=cl  <br>"
        "4.Dr.R. Baghya Nisha https://in.docworkspace.com/d/sILm4hYOQApj6sLcG?sa=cl  <br>"
        "5.Er.R. Shailajha https://in.docworkspace.com/d/sIGi4hYOQAqn6sLcG?sa=cl  <br>"
        "6.Er. Vimal,H https://in.docworkspace.com/d/sIKK4hYOQArr6sLcG?sa=cl  <br>"
        "7.Er.S. Indumathi https://in.docworkspace.com/d/sIG64hYOQAsb6sLcG?sa=cl  <br>"
        "They are the faculty of FT in 2025-26. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "good afternoon",
        "questions": [
            "happy afternoon.",
            "good afternoon.",
            "hi, good afternoon."
        ],
        "answer": "hello, good afternoon."
    },
    {
        "id": "good night",
        "questions": [
            "have a good night.",
            "good night",
            "hi, good night."
        ],
        "answer": "hello, good night."
    },
    {
        "id": "happy morning.",
        "questions": [
            "happy morning.",
            "good morning.",
            "hi good morning."
        ],
        "answer": "good morning, how can I help you."
    },
    {
        "id": "image_of_clg",
        "questions": [
            "manakula vinayagar institute of technology images",
            "mvit photos",
            "mvit images"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "iot_staff",
        "questions": [
            "information of things faculty",
            "IOT teachers",
            "iot mentors",
            "iot facultys",
            "iot professors",
            "io t staffs",
            "i ot staff"
        ],
        "answer": "1.Dr.N. PALANIVEL (HOD) <br>"
        "2.Mr.V.KUMARAGURU <br> https://i.ibb.co/Hpn3Pgk8/Screenshot-20250918-115645.jpg <br>"
        "3.Mrs.K.C NITHYASREE <br> https://i.ibb.co/M58VJh3H/Screenshot-20250918-115659.jpg <br>"
        "4.Ms.S.ADOLPHINE SHYNI <br> https://i.ibb.co/5WN4bSmL/Screenshot-20250918-115715.jpg  <br>"
        "5.Mrs.K.KAVITHA <br> https://i.ibb.co/RTW7wQqG/Screenshot-20250918-115729.jpg <br>"
        "6.Ms.A.SHEERIN <br> https://i.ibb.co/NdcrZFhQ/Screenshot-20250918-115748.jpg <br>"
        "They are the faculty of IOT in 2025-26. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "Library",
        "questions": [
            "library in manakula vinayagar institute of technology",
            "mvit library images",
            "library images",
            "library in our clg",
            "library"
        ],
        "answer": "img:/static/images/library.jpeg"
    },
    {
        "id": "mech_staff",
        "questions": [
            "mech staff",
            "mech teacher",
            "mech faculty",
            "mech professors",
            "mechanical engineering faculty"
        ],
        "answer": "1.Dr.B.RADJARAM <br> https://i.ibb.co/CKkZtChw/Screenshot-20250918-120858.jpg <br>"  
        "2.Mr.B.VASANTH <br> https://i.ibb.co/JRp2dNm9/Screenshot-20250918-121346.jpg <br>"
        "3.Mr.J.SUGUMARAN <br> https://i.ibb.co/BVy3BjW1/Screenshot-20250918-121410.jpg <br>" 
        "4.Mr.R.RANJIT KUMAR <br> https://i.ibb.co/8Gc56Wh/Screenshot-20250918-121425.jpg <br>"         
        "5.Ms.S.SUGUNYA <br> https://i.ibb.co/Q3JMyV7G/Screenshot-20250918-121442.jpg <br>" 
        "6.Mr.R.ILANDJEZIANR <br> https://i.ibb.co/zW8LYWhR/Screenshot-20250918-121500.jpg <br>" 
        "7.Dr.A.MATHIARASU <br> https://i.ibb.co/d0966y6F/Screenshot-20250918-121522.jpg  <br>"
        "8.Dr.P.NATARAJAN <br> https://i.ibb.co/Df40TSvX/Screenshot-20250918-121548.jpg  <br>"
        "9.Mrs.G.DEEBA <br> https://i.ibb.co/PZyLdCtd/Screenshot-20250918-121613.jpg  <br>"
        "10.Mrs.S.SHEENA <br> https://i.ibb.co/Y7RDfgnw/Screenshot-20250918-121623.jpg  <br>"
        "They are the faculty of MECH in 2025-26. <br> You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "placement",
        "questions": [
            "placements in mvit",
            "placement in our clg",
            "student selected in company",
            "student got placement",
            "students placement record",
            "students placement",
            "placement",
            "placement records",
            "placement details"
        ],
        "answer": "Mvit has 90% placement records"
    },
    {
        "id": "queries_form",
        "questions": [
            "queries submission link",
            "queries link",
            "queries submission",
            "I have some queries",
            "queries form",
            "queries section",
            "where did i submit my queries",
            "queries",
            "complaint"
        ],
        "answer": "You can submit your queries by using the link <br> https://docs.google.com/forms/d/e/1FAIpQLSe5kYktZG884dUGs7As2CxX240i5yq9O4pBoL4n6sJYITlRTA/viewform?usp=sf_link"
    },
    {
        "id": "robotics_staff",
        "questions": [
            "ra staff",
            "robotics staff",
            "robotics and automation mentor",
            "robotics and automation teachers",
            "robotics and automation professors",
            "robotics and automation faculty",
            "robotics and automation staff"
        ],
        "answer": "1.Dr.V.GOVINDHAN <br> https://i.ibb.co/JRBtXGxp/Screenshot-20250918-135947.jpg  <br>"
        "2.Mr.A.BASKARAN <br> https://i.ibb.co/VYXYCPyj/Screenshot-20250918-140000.jpg  <br>"
        "3.Mrs.S.Ramya <br> https://i.ibb.co/H1XC1P7/Screenshot-20250918-140054.jpg <br>"
        "4.Mrs.J.V. PESHA <br> https://i.ibb.co/gFFVxDSF/Screenshot-20250918-140018.jpg <br>"
        "5.Mrs.D.DHARANI <br> https://i.ibb.co/HTqW7369/Screenshot-20250918-140033.jpg <br>"
        "6.Mrs.T.SUDHA <br> https://i.ibb.co/pBpTxB0p/Screenshot-20250918-140044.jpg <br>"
        "They are the faculty of robotics and automation in 2025-26.<br> You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "room_num",
        "questions": [
            "class rooms allotment in manakula vinayagar institute of technology",
            "number of classes",
            "classes",
            "class room details",
            "room numbers",
            "class room allotment",
            "class rooms in mvit clg"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "seats_for_cse",
        "questions": [
            "seat for computer science engineering",
            "seat for cse",
            "seat for cse in mit",
            "no of seats in cse",
            "how many seats are there for cse",
            "how many seat alloted for cse",
            "cse seats"
        ],
        "answer": "no of seats for computer science engineering in B.TECH in 2025 is... [240] and in M.TECH is ...[12]"
    },
    {
        "id": "seats_for_ece",
        "questions": [
            "seats for electronics communication engineering",
            "seat for ece",
            "seat for ece in mit",
            "no of seats in ece",
            "how many seats are there for ece",
            "how many seat alloted for ece",
            "ece seats"
        ],
        "answer": "no of seats for electronics and communication engineering  in B.TECH in 2025 is... [180] and in M.TECH is...[12]"
    },
    {
        "id": "seats_for_FT",
        "questions": [
            "seat for food technology",
            "seat for ft",
            "seat for ft in mit",
            "no of seats in ft",
            "how many seats are there for ft",
            "how many seat alloted for ft"
        ],
        "answer": "no of seats for food technology  in 2025 is... [60]"
    },
    {
        "id": "seats_for_Iot",
        "questions": [
            "seats in information of things",
            "seat for iot",
            "seat for iot in mit",
            "no of seats in iot",
            "how many seats are there for iot",
            "how many seat alloted for iot"
        ],
        "answer": "no of seats for information of things in 2025 is... [60]"
    },
    {
        "id": "seats_for_MECH",
        "questions": [
            "seat in mechanical engineering",
            "seats in mechanical",
            "seat for mech",
            "seat for mech in mit",
            "no of seats in mech",
            "how many seats are there for mech",
            "how many seat alloted for mech",
            "mech seats"
        ],
        "answer": "no of seats for mechanical engineering in 2025 is... [60]"
    },
    {
        "id": "seats_for_robotics",
        "questions": [
            "seat for robotics",
            "seat for RA in mit",
            "no of seats in robotics",
            "how many seats are there for RA",
            "how many seat alloted for RA"
        ],
        "answer": "no of seats for robotics in 2025 is... [60]"
    },
    {
        "id": "seat_for_aiml",
        "questions": [
            "seats for artificial engineering and machine learning",
            "aiml seats",
            "how many seat alloted for aiml",
            "how many seats are there for aiml",
            "no of seats in aiml",
            "seat for aiml in mit",
            "seat for aiml"
        ],
        "answer": "no of seats for artificial and machine learning in 2025 is... [180]"
    },
    {
        "id": "seat_for_eee",
        "questions": [
            "electrical and electronics engineering",
            "eee seat in 2024",
            "seat for eee",
            "seat for eee in mit",
            "no of seats in eee",
            "how many seats are there for eee",
            "how many seat alloted for eee",
            "eee seats"
        ],
        "answer": "no of seats for electrical and electronics engineering in 2025 is... [60]"
    },
    {
        "id": "seat_for_IT",
        "questions": [
            "seats for information technology",
            "seat for it",
            "seat for it in mit",
            "no of seats in it",
            "how many seats are there for it",
            "how many seat alloted for it",
            "it seats"
        ],
        "answer": "no of seats for information technology in 2025 is... [120]"
    },
    {
        "id": "sports",
        "questions": [
            "sports activity",
            "sports award",
            "extra cricular activity eca",
            "sports in mvit",
            "sports",
            "sports in your clg",
            "what are the sports in our clg"
        ],
        "answer": "silver medal in 100m swimming competition"
    },
    {
        "id": "syllabus_aiml_sem1",
        "questions": [
            "aiml syllabus for semester1",
            "sem1 aiml syllabus",
            "sem1 syllabus for aiml",
            "aiml sem1 syllabus",
            "phy syllabus for aiml",
            "m1 syllabus for aiml",
            "bee syllabus for aiml",
            "semester 1 syllabus for aiml",
            "syllabus for aiml sem 1",
            "syllabus for aiml",
            "aiml syllabus"
        ],
        "answer": "sem1 syllabus for aiml is given below"
    },
    {
        "id": "syllabus_aiml_sem2",
        "questions": [
            "aiml syllabus for semester2",
            "aiml syllabus for 2semester",
            "aiml syllabus 2sem",
            "sem2 syllabus for aiml",
            "aiml sem2 syllabus"
        ],
        "answer": "Problem solving and programming"
    },
    {
        "id": "syllabus_aiml_sem3",
        "questions": [
            "sem3 aiml",
            "aiml sem3",
            "syllabus for aiml semester3",
            "aiml semester3 syllabus",
            "sem3 syllabus aiml",
            "syllabus for sem3 aiml",
            "syllabus for aiml sem3"
        ],
        "answer": "These are the sem3 syllabus for aiml"
    },
    {
        "id": "syllabus_cse_sem1",
        "questions": [
            "cse syllabus",
            "syllabus for computer science engineering",
            "semester1 cse syllabus",
            "cse syllabus for sem1"
        ],
        "answer": "BEE syllabus"
    },
    {
        "id": "vision_mission",
        "questions": [
            "clg mission",
            "clg vision",
            "vision and mission",
            "clg vision and mission",
            "vision and mission of the manakula vinayagar institute of technology collage",
            "vision and mission of the mvit collage"
        ],
        "answer": "img:/static/images/vision.jpeg"
    },
    {
        "id": "College Building Image",
        "questions": [
            "college building image",
            "mvit building photo",
            "photo of college",
            "clg pic",
            "campus building picture"
            "college",
            "collage",
            "images of a clg"
        ],
        "answer": "img:/static/images/college.jpeg"
    },
    {
        "id": "Hostel Image",
        "questions": [
            "hostel image",
            "clg hostel photo",
            "show me hostel picture",
            "mvit hostel pic",
            "hostel",
            "hostal",
            "hostel in mvit",
            "boys hostel",
            "girls hostel"
        ],
        "answer": "img:/static/images/hostal.jpeg" 
    },
    {
        "id": "Sports Ground Image",
        "questions": [
            "sports ground image",
            "playground photo",
            "mvit sports pic",
            "clg ground picture"
        ],
        "answer": "img:/static/images/sports.jpg"  
    },
    {
        "id": "user intraction",
        "questions": [
            "mvit bot",
            "he bot",
            "chat bot",
            "MVIT bot",
            "mit bot"
        ],
        "answer": "yeah,Tell me, How can I hell you?"
    },
    {
        "id": "boys Hostel",
        "questions": [
            "boys hostel image",
            "boys hostel photo",
            "show me hostel picture of boy",
            "mvit boys hostel pic",
            "boys hostel",
            "boys hostal",
            "boys hostel in mvit",
            "boys hostel",
            "boys hostel"
        ],
        "answer": "img:/static/images/boys_hostel.jpeg" 
    },
    {
        "id": "girls Hostel",
        "questions": [
            "girls hostel image",
            "girls hostel photo",
            "show me hostel picture of girls",
            "mvit girls hostel pic",
            "girl hostel",
            "girls hostal",
            "girl hostel in mvit",
            "girl hostel",
            "girls hostel"
        ],
        "answer": "img:/static/images/hostal.jpeg" 
    },
    {
        "id": "PET ground",
        "questions": [
            "mvit pt ground",
            "mit pet ground",
            "MVIT p.e.t ground",
            "sports ground in mvit",
            "sports place",
            "ground"
        ],
        "answer": "img:/static/images/pet_ground.jpeg"
    },
    {
        "id": "volleyball ground",
        "questions": [
            "mvit volleyball ground",
            "mit volley ball ground",
            "MVIT volley ball ground",
            "volley ground in mvit",
            "volley ball place",
            "volleyball ground",
            "volleyball",
            "volley ball"
        ],
        "answer": "img:/static/images/volleyball_ground.jpeg"
    },
    {
        "id": "basketball ground",
        "questions": [
            "mvit Basketball ground",
            "mit basket ground",
            "MVIT basket_ball ground",
            "basket ground in mvit",
            "basket ball place",
            "basketball ground",
            "basketball",
            "basket ball"
        ],
        "answer": "img:/static/images/basketball_ground.jpeg"
    },
    {
        "id": "companies",
        "questions": [
            "no of companies in mvit clg",
            "number of company are there in mit",
            "how many companies are in mvit",
            "companies",
            "no of company"
        ],
        "answer": "MVIT has tie up with 50+ companies"
    },
    {
        "id": "companies",
        "questions": [
            "what are the companies in mvit",
            "company collab with mit",
            "some company tie up with mvit",
            "what company are partnership with mvit",
            "name the company collabrated with MVIT",
            "comapanies names",
            "company name",
            "name of the company",
            "what are the company in mvit"
        ],
        "answer": "Google,<br> Microsoft,<br> TCS,<br> Virtusa,<br> Zoho etc"
    },
    {
        "id": "no of students",
        "questions": [
            "no of students in mvit",
            "number of students studying in mvit",
            "total of students in mvit",
            "how many students are there in mvit",
            "mit students",
            "total no of students in mit"
        ],
        "answer": "MVIT currently has 3000+ students"
    },
    {
        "id":"no of labs",
        "questions": [
            "no of labs in mvit",
            "number of lab in mvit",
            "total of labs in mvit",
            "how many Lab are there in mvit",
            "mit LABS",
            "total no of labs in mit"
        ],
        "answer": "MVIT has Total 11 labs"
    },
    {
        "id":"principal",
        "questions": [
            "principal",
            "principle of mvit",
            "principal of mit",
            "who is the principal of mvit",
            "tell me the name of the principal",
            "mvit principal"
        ],
        "answer": "Dr.S.Malarkkan is our collage Principal"
    },
    {
        "id":"trustee",
        "questions": [
            "trustee",
            "trustee of mvit",
            "truste of mit",
            "who is the trustee of mvit",
            "tell me the name of the trustee",
            "mvit trustree"
        ],
        "answer": "Mrs.V.Nirmala<br> Mrs.D.Geetha<br> They are the trustee of our college"
    },
    {
        "id":"vice chairperson",
        "questions": [
            "vice chairperson",
            "vice charperson of mvit",
            "vice charperson",
            "who is the vice chairperson of mvit",
            "tell me the name of the vicecharperson",
            "mvit vicechairperson",
            "vicechairperson"
        ],
        "answer": " Mrs.K.Nalini is the vice chairperson of our collage"
    },
    {
        "id":"secretary",
        "questions": [
            "secretary",
            "secretary of mvit",
            "secretary",
            "who is the secretary of mvit",
            "tell me the name of the secretary",
            "mvit secretary",
            "secretary"
        ],
        "answer": " Mrs.K.Nalini is the vice chairperson of our collage"
    },
    {
        "id":"secretary",
        "questions": [
            "secretary",
            "secretary of mvit",
            "secretary",
            "who is the secretary of mvit",
            "tell me the name of the secretary",
            "mvit secretary",
            "secretary"
        ],
        "answer": " Mrs.K.Nalini is the vice chairperson of our collage"
    },
    {
        "id":"secretary",
        "questions": [
            "secretary",
            "secretary of mvit",
            "secretary",
            "who is the secretary of mvit",
            "tell me the name of the secretary",
            "mvit secretary",
            "secretary"
        ],
        "answer": " Mrs.K.Nalini is the vice chairperson of our collage"
    },
    {
        "id":"Treasurer",
        "questions": [
            "Treasurer",
            "treasurer of mvit",
            "treasurer",
            "who is the treasurer of mvit",
            "tell me the name of the treasurer",
            "mvit treasurer",
            "treasurer"
        ],
        "answer": "Shri.S.V. Sugamaran is the vice Treasurer of our collage"
    },
    {
        "id":"chairman",
        "questions": [
            "chairman",
            "chairman of mvit",
            "Chairman",
            "who is the Chairman of mvit",
            "tell me the name of the chairman",
            "mvit CHAIRMAIN",
            "Chairman"
        ],
        "answer": "M. Dhanasekaran is the Chairman of our collage"
    },
    {
        "id":"founder",
        "questions": [
            "founder",
            "founder of mvit",
            "founder",
            "who is the founder of mvit",
            "tell me the name of the founder",
            "mvit FOUNDER",
            "founder"
        ],
        "answer": "N.Kesavan is the Founder of our collage"
    },
    {
        "id": "creator",
        "questions": [
            "who created you",
            "creator",
            "creater",
            "who makes you",
            "who is your boss",
            "who makes you",
            "maker",
            "give creater name",
            "name of the creator",
            "your owner",
            "woned by who",
            "who woned you"
        ],
        "answer": "Mr.R.Avinash is my creator"
    },
    {
        "id": "purpose",
        "questions": [
            "purpose",
            "what purpose do you created",
            "what is your purpose",
            "tell me your features",
            "what is your feature",
            "purpose of mvit chatbot",
            "purpose of ak chatbot",
            "narrow chatbot purpose",
            "purpose of narrow chatbot",
            "purpose of you",
            "purpose of the chatbot",
            "why you made",
            "why you make"
        ],
        "answer": "I’m a fast, I understand and generate clear responses on many topics and available 24/7, Multiple user can easily access me at same time, turn complex search into simple input, so you save time and get practical answers quickly."
    },
    {
        "id": "placement percentage",
        "questions": [
            "How many students are graduated in mvit",
            "graduation percrntage in mvit"
            "no of placed percentage in mvit",
            "placement percentage",
            "percentage of placed students",
            "How many students are placement in mvit",
            "what is percentage of placement in mvit",
            "mvit placements",
            "placement record",
            "placement record in mvit",
            "placement"
        ],
        "answer": "Manakula vinayagar Institute of Technology has 90% placement records "
    },
    {
        "id": "contact number",
        "questions": [
            "phone number",
            "contact details",
            "contact information",
            "mvit phonenumber",
            "mit mobile number",
            "mit mail id",
            "mail",
            "mail id",
            "mail information",
            "give mail id and phone number",
            "give phone number and mail id",
            "how can we contact you",
            "phone",
            "contact"
        ],
        "answer": "You can contact MVIT through <br> Phone- 0413-2643007, <br> 9498093535 <br> Mail- principal@mvit.edu.in"
    },
    {
        "id":"events",
        "questions": [
            "events in mvit",
            "events",
            "what are the events in mvit",
            "events conducted in mvit",
            "elan 2025",
            "programs",
            "programs in mvit clg",
            "elan"
        ],
        "answer": "img:/static/images/elan_event.jpeg"
    },
    {
        "id": "no of computer",
        "questions":[
            "number of computer are there in mvit",
            "how many system are in mvit",
            "no of system in mvit",
            "systems in mvit",
            "how many desktop are in mvit labs",
            "how much computer used for work in mvit",
            "computers in mvit"
        ],
        "answer":"Mvit has 558 computers"
    },
    {
        "id": "no of server",
        "questions":[
            "number of servers are there in mvit",
            "servers",
            "total servers in mvit",
            "Total servers"
        ],
        "answer":"Mvit has 6 servers"
    },
    {
        "id": "network",
        "questions":[
            "network used",
            "network",
            "internet in mvit",
            "which network is used in mvit"
        ],
        "answer":"Mvit has BSNL internet service"
    },
    {
        "id": "cells",
        "questions":[
            "cells in mvit",
            "cells",
            "cell",
            "committes in mvit",
            "what are the cells are in mvit",
            "cells of mvit",
            "what are the committe are in mvit",
            "committe of mvit",
            "committe",
            "committes"
        ],
        "answer":"1.Academic Planning committee <br>"
                 "2.Quality Assessment Committee (QAC) <br>"
                 "3.Academic Audit committee <br>"
                 "4.Budget and finance committee <br>"
                 "5.College News Letter, Magazine, Prospectus committee <br>"
                 "6.Sports committee <br>"
                 "7.Cultural committee <br>"
                 "8.Anti-ragging committee <br>"
                 "9.Grievances Redressal committee <br>"
                 "10.Transport committee <br>"
                "11.Discipline Committee <br>"
                "12.Mentoring Committee and counseling <br>"
                "13.Purchase committee <br>"
                "14.Infrastructure Management / Time table committee <br>"
                "15.HoDs committee <br>"
                "16.Hods sub committee <br>"
                "17.Canteen committee <br>"
                "18.Hostel committee <br>"
                "19.Code of Conduct Committee <br> These are the committes/cells of MVIT."
    },
    {
       "id": "no of cells",
        "questions":[
            " no ofcells in mvit",
            "how many cells are in mvit",
            "total no of cells",
            "no of committes in mvit",
            "total no of committee are in mvit",
        ],
        "answer":"No of cells/committee in MVIT is 19" 
    },
    {
        "id": "link",
        "questions":[
            "link",
            "give me the link",
            "i want link",
            "send the link"
        ],
        "answer": "https://mvit.edu.in/<br> (you can visit our clg website)"
    },
    {
        "id":"bye",
        "questions":[
        "bye",
        "taata",
        "good bye",
        "i am going",
        "see you later",
        "leaving",
        "see you back"
        ],
        "answer":"bye👋! Have a nice day"
    },
    {
        "id": "AIML_HOD",
        "questions": [
            "aiml HOD",
            "aiml hod",
            "hod aiml"
        ],
        "answer":"Mr.R. RAJ BHARATH is the HOD of AIML."
    },
    {
        "id": "cse_hod",
        "questions": [
            "cse hod",
            "CSE hod",
            "Cse hod",
            "computer science engineering hod",
            "hod of cse",
            "who is the hod of cse"
        ],
        "answer":""
    }

]

# -------------------- PREPROCESS --------------------
question_to_answer = {}
all_questions = []

for entry in qa_data:
    for q in entry["questions"]:
        ql = q.lower().strip()
        question_to_answer[ql] = entry["answer"]
        all_questions.append(ql)

spell = SpellChecker()

def find_best_match(user_input):
    ui = (user_input or "").lower().strip()
    if not ui:
        return "Please type a question."
    if ui in question_to_answer:
        return question_to_answer[ui]
    match = difflib.get_close_matches(ui, all_questions, n=1, cutoff=0.70)
    if match:
        return question_to_answer[match[0]]
    return "Answer not available."
    import stmplib
    host ="smtp.gamil.com"
    port = 587
    usmail= "databasemvit@gmail.com"
    pw = "Database@2000"
    

# -------------------- ROUTES --------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    data = request.get_json(force=True) or {}
    user_message = data.get('msg', '')

    words = user_message.lower().split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = " ".join(corrected_words)

    reply = find_best_match(corrected_text)

    # If reply is an image path, return image in response
    if reply.startswith("/static/"):
        return jsonify({"reply": "Here is the picture you asked for:", "image": reply})
    else:
        return jsonify({"reply": reply, "image": None})

if __name__ == '__main__':
    app.run(debug=True)
