# -*- coding: utf-8 -*-
"""
بنك الأسئلة الثنائي اللغة — أساسيات الحاسوب
Bilingual question bank — Computer Fundamentals
إعداد الطالب باسم عصيد كمر / Prepared by Basim Aseed Kamar

البنية موحّدة بين اللغتين: لكل لغة نفس عدد الأسئلة ونفس الترتيب.
The structure is identical across languages: same questions, same order.

  definitions  → تعاريف   (20)
  mcq          → اختيارات (22)
  true_false   → صح وخطأ  (22)
  MID_EXAM     → امتحان الميد (10, أسئلة مقالية / open-ended)

كل سؤال اختياري: {"q": .., "options": [..], "correct": idx, "exp": ..}
كل سؤال ميد:     {"q": .., "a": الإجابة النموذجية}
"""

import random

QUESTIONS = {
    # ====================================================================
    # ENGLISH
    # ====================================================================
    "en": {
        "definitions": [
            {"q": "What is a computer?",
             "options": ["An electronic device that processes data into information",
                         "A type of printer", "A storage box for papers", "A kind of network cable"],
             "correct": 0, "exp": "A computer takes data as input and processes it into useful information."},
            {"q": "What is hardware?",
             "options": ["The physical parts of the computer you can touch",
                         "The set of programs and instructions", "A website on the internet", "A type of computer virus"],
             "correct": 0, "exp": "Hardware = the tangible physical components (CPU, RAM, keyboard...)."},
            {"q": "What is software?",
             "options": ["The set of instructions (programs) that tell the computer what to do",
                         "The metal case of the computer", "The power cable", "The monitor screen"],
             "correct": 0, "exp": "Software is the programs/instructions; hardware carries them out."},
            {"q": "What is the CPU?",
             "options": ["The brain of the computer that controls and processes",
                         "A device for printing documents", "A type of external memory", "The computer's power supply"],
             "correct": 0, "exp": "The CPU (Central Processing Unit) is the brain: it controls and processes."},
            {"q": "What is RAM?",
             "options": ["Fast temporary main memory that loses data when power is off",
                         "Permanent storage that keeps data forever", "An input device", "A web browser"],
             "correct": 0, "exp": "RAM is volatile main memory: its contents are lost when power is off."},
            {"q": "What is an operating system?",
             "options": ["System software that manages the hardware and resources (e.g. Windows)",
                         "An application for editing photos", "A type of input device", "A web protocol"],
             "correct": 0, "exp": "The OS is system software that runs the computer and manages resources."},
            {"q": "What is a URL?",
             "options": ["The full address of a web page", "A type of computer virus",
                         "An output device", "A unit of memory"],
             "correct": 0, "exp": "URL = Uniform Resource Locator: the full address of a web page."},
            {"q": "What is a computer virus?",
             "options": ["A small program that spreads and can damage data",
                         "A useful tool that speeds up the computer", "A type of monitor", "An official operating system"],
             "correct": 0, "exp": "A virus is malicious code that spreads and can damage or destroy data."},
            {"q": "What is cache memory?",
             "options": ["Very fast memory close to the CPU that speeds up access",
                         "The largest and slowest storage device", "An input device", "A type of printer"],
             "correct": 0, "exp": "Cache is small, very fast memory near the CPU (L1, L2, L3)."},
            {"q": "What is a firewall?",
             "options": ["A system that filters network traffic and blocks threats",
                         "A program that creates viruses", "A type of keyboard", "A unit for measuring memory"],
             "correct": 0, "exp": "A firewall filters traffic by rules and helps block hackers and worms."},
            {"q": "What is ROM?",
             "options": ["Permanent memory that stores startup instructions and keeps data without power",
                         "Temporary memory that loses data when power is off", "An input device", "A web browser"],
             "correct": 0, "exp": "ROM is non-volatile memory; it keeps its data even without power."},
            {"q": "What is a bit?",
             "options": ["The smallest unit of data, either 0 or 1", "A group of 8 characters",
                         "One thousand bytes", "A type of input device"],
             "correct": 0, "exp": "A bit is the smallest unit of data: 0 or 1."},
            {"q": "What is a byte?",
             "options": ["A group of 8 bits", "A single 0 or 1", "One million bits", "An output device"],
             "correct": 0, "exp": "1 byte = 8 bits."},
            {"q": "What is the ALU?",
             "options": ["The part of the CPU that performs arithmetic and logic operations",
                         "The main storage device", "A type of monitor", "The power supply"],
             "correct": 0, "exp": "ALU = Arithmetic Logic Unit; it does calculations and comparisons."},
            {"q": "What is the Control Unit (CU)?",
             "options": ["The part of the CPU that directs and coordinates operations",
                         "Memory that stores files permanently", "An input device", "A network cable"],
             "correct": 0, "exp": "The CU directs the operations of the CPU and the other parts."},
            {"q": "What is a web browser?",
             "options": ["Software used to access and view web pages",
                         "A device that prints documents", "A type of memory", "An internet cable"],
             "correct": 0, "exp": "A browser (e.g. Chrome) lets you view web pages."},
            {"q": "What is the Internet?",
             "options": ["A global network that connects millions of computers worldwide",
                         "A single website", "A type of computer virus", "An output device"],
             "correct": 0, "exp": "The Internet is the worldwide network connecting computers."},
            {"q": "What is the World Wide Web (WWW)?",
             "options": ["A service of linked web pages accessed over the Internet",
                         "The physical cables of the Internet", "A type of CPU", "A storage device"],
             "correct": 0, "exp": "The Web is a service of linked pages running on the Internet."},
            {"q": "What is an output device?",
             "options": ["A device that sends information out from the computer to the user",
                         "A device that feeds data into the computer", "A part of the CPU", "A type of cable"],
             "correct": 0, "exp": "Output devices (monitor, printer) deliver results to the user."},
            {"q": "What is application software?",
             "options": ["Programs that let the user do specific tasks (e.g. Word, Chrome)",
                         "Software that manages the hardware and resources", "The physical parts of the computer", "A type of virus"],
             "correct": 0, "exp": "Application software performs specific user tasks."},
        ],
        "mcq": [
            {"q": "Which of these is an INPUT device?",
             "options": ["Keyboard", "Monitor", "Printer", "Speakers"], "correct": 0,
             "exp": "A keyboard sends data INTO the computer, so it is an input device."},
            {"q": "Which of these is an OUTPUT device?",
             "options": ["Printer", "Mouse", "Scanner", "Microphone"], "correct": 0,
             "exp": "A printer sends information OUT to the user, so it is an output device."},
            {"q": "Which bus carries the memory addresses?",
             "options": ["Address bus", "Data bus", "Control bus", "USB bus"], "correct": 0,
             "exp": "The address bus carries the location (address) of the data in memory."},
            {"q": "What is the smallest unit of data?",
             "options": ["Bit", "Byte", "Kilobyte", "Megabyte"], "correct": 0,
             "exp": "A bit (0 or 1) is the smallest unit; 8 bits make 1 byte."},
            {"q": "One byte equals how many bits?",
             "options": ["8 bits", "2 bits", "16 bits", "1024 bits"], "correct": 0, "exp": "1 byte = 8 bits."},
            {"q": "Which computer generation used vacuum tubes?",
             "options": ["First generation", "Third generation", "Fourth generation", "Fifth generation"],
             "correct": 0, "exp": "The first generation (1940-1956) used vacuum tubes."},
            {"q": "Which of these is SYSTEM software?",
             "options": ["Windows", "Microsoft Word", "Google Chrome", "Photoshop"], "correct": 0,
             "exp": "Windows is an operating system = system software; the others are applications."},
            {"q": "Which protocol is the SECURE version for the web?",
             "options": ["HTTPS", "HTTP", "FTP", "ISP"], "correct": 0,
             "exp": "HTTPS is the secure, encrypted version of HTTP."},
            {"q": "Which malware pretends to be useful but hides harmful actions?",
             "options": ["Trojan horse", "Spyware", "Adware", "Worm"], "correct": 0,
             "exp": "A Trojan horse looks useful but secretly hides harmful actions."},
            {"q": "Order from smallest to largest:",
             "options": ["KB < MB < GB < TB", "TB < GB < MB < KB", "MB < KB < GB < TB", "GB < MB < TB < KB"],
             "correct": 0, "exp": "Kilobyte < Megabyte < Gigabyte < Terabyte."},
            {"q": "Which bus carries the actual data between the CPU and memory?",
             "options": ["Data bus", "Address bus", "Control bus", "Power bus"], "correct": 0,
             "exp": "The data bus carries the actual data values."},
            {"q": "Which of these is NOT an input device?",
             "options": ["Monitor", "Keyboard", "Mouse", "Scanner"], "correct": 0,
             "exp": "A monitor is an output device, not an input device."},
            {"q": "Which memory is volatile (loses data when power is off)?",
             "options": ["RAM", "ROM", "Hard disk", "SSD"], "correct": 0,
             "exp": "RAM is volatile; the others keep data without power."},
            {"q": "Which is the LARGEST unit of memory?",
             "options": ["Terabyte", "Kilobyte", "Megabyte", "Gigabyte"], "correct": 0,
             "exp": "TB is the largest: KB < MB < GB < TB."},
            {"q": "Which computer generation used transistors?",
             "options": ["Second generation", "First generation", "Fourth generation", "Fifth generation"],
             "correct": 0, "exp": "The second generation used transistors."},
            {"q": "Which of these is an APPLICATION software?",
             "options": ["Microsoft Word", "Windows", "Linux", "macOS"], "correct": 0,
             "exp": "Word is an application; the others are operating systems."},
            {"q": "Which protocol is used to transfer files?",
             "options": ["FTP", "HTTP", "HTTPS", "ISP"], "correct": 0, "exp": "FTP = File Transfer Protocol."},
            {"q": "Which malware secretly collects your data and browsing habits?",
             "options": ["Spyware", "Adware", "Worm", "Firewall"], "correct": 0,
             "exp": "Spyware secretly collects your information."},
            {"q": "In a URL, which part is 'https'?",
             "options": ["The protocol", "The domain name", "The path", "The file size"], "correct": 0,
             "exp": "'https' is the protocol part of the URL."},
            {"q": "The CPU is also known as the...?",
             "options": ["Processor (brain of the computer)", "Monitor", "Power supply", "Hard drive"],
             "correct": 0, "exp": "The CPU is the processor, the brain of the computer."},
            {"q": "Which device shows output visually on a screen?",
             "options": ["Monitor", "Speaker", "Keyboard", "Microphone"], "correct": 0,
             "exp": "The monitor displays visual output."},
            {"q": "How many basic functions does a computer have?",
             "options": ["Four (input, processing, output, storage)", "Two", "Six", "Three"], "correct": 0,
             "exp": "Input, processing, output and storage = four functions."},
        ],
        "true_false": [
            {"q": "Software is the physical part of the computer.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — software is the programs; the physical part is hardware."},
            {"q": "The CPU is called the brain of the computer.",
             "options": ["True", "False"], "correct": 0, "exp": "True — the CPU controls and processes, like a brain."},
            {"q": "RAM keeps its data even when the power is turned off.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — RAM is volatile; it loses its data when power is off."},
            {"q": "HTTPS is more secure than HTTP.",
             "options": ["True", "False"], "correct": 0, "exp": "True — HTTPS is the encrypted, secure version."},
            {"q": "A worm needs human help to spread.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — worms self-activate and copy themselves without human help."},
            {"q": "The Internet and the World Wide Web are exactly the same thing.",
             "options": ["True", "False"], "correct": 1, "exp": "False — the Web is a service that runs on top of the Internet."},
            {"q": "An SSD is generally faster than an HDD.",
             "options": ["True", "False"], "correct": 0, "exp": "True — an SSD has no moving parts and is faster than an HDD."},
            {"q": "A firewall can help block hackers and worms.",
             "options": ["True", "False"], "correct": 0, "exp": "True — a firewall filters traffic and blocks threats."},
            {"q": "1 KB is larger than 1 MB.",
             "options": ["True", "False"], "correct": 1, "exp": "False — 1 MB is larger; KB < MB < GB < TB."},
            {"q": "Antivirus software should be kept up to date.",
             "options": ["True", "False"], "correct": 0, "exp": "True — updates let it detect the newest threats."},
            {"q": "ROM is non-volatile memory (it keeps data without power).",
             "options": ["True", "False"], "correct": 0, "exp": "True — ROM keeps its data even when power is off."},
            {"q": "A scanner is an output device.",
             "options": ["True", "False"], "correct": 1, "exp": "False — a scanner is an input device."},
            {"q": "The control unit performs the arithmetic operations.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — the ALU does arithmetic; the control unit directs operations."},
            {"q": "A megabyte is larger than a kilobyte.",
             "options": ["True", "False"], "correct": 0, "exp": "True — 1 MB = 1024 KB."},
            {"q": "The first generation of computers used transistors.",
             "options": ["True", "False"], "correct": 1, "exp": "False — the first generation used vacuum tubes."},
            {"q": "A web browser is an example of application software.",
             "options": ["True", "False"], "correct": 0, "exp": "True — a browser is application software."},
            {"q": "The address bus carries the actual data values.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — the address bus carries addresses; the data bus carries data."},
            {"q": "Spyware secretly collects user information.",
             "options": ["True", "False"], "correct": 0, "exp": "True — spyware secretly gathers your data."},
            {"q": "HTTP is more secure than HTTPS.",
             "options": ["True", "False"], "correct": 1, "exp": "False — HTTPS is the secure one."},
            {"q": "Cache memory is slower than RAM.",
             "options": ["True", "False"], "correct": 1,
             "exp": "False — cache is faster than RAM and closer to the CPU."},
            {"q": "A printer is an input device.",
             "options": ["True", "False"], "correct": 1, "exp": "False — a printer is an output device."},
            {"q": "The motherboard connects the computer's components together.",
             "options": ["True", "False"], "correct": 0, "exp": "True — the motherboard links all the components."},
        ],
    },

    # ====================================================================
    # ARABIC — نفس التقسيم ونفس الأسئلة بالضبط
    # ====================================================================
    "ar": {
        "definitions": [
            {"q": "ما هو الحاسوب؟",
             "options": ["جهاز إلكتروني يعالج البيانات ويحوّلها إلى معلومات",
                         "نوع من أنواع الطابعات", "صندوق لحفظ الأوراق", "نوع من كابلات الشبكة"],
             "correct": 0, "exp": "الحاسوب يأخذ البيانات كمدخلات ويعالجها إلى معلومات مفيدة."},
            {"q": "ما هو العتاد (Hardware)؟",
             "options": ["الأجزاء المادية الملموسة في الحاسوب",
                         "مجموعة البرامج والتعليمات", "موقع على الإنترنت", "نوع من فيروسات الحاسوب"],
             "correct": 0, "exp": "العتاد = المكوّنات المادية الملموسة (المعالج، الذاكرة، لوحة المفاتيح...)."},
            {"q": "ما هي البرمجيات (Software)؟",
             "options": ["مجموعة التعليمات (البرامج) التي تخبر الحاسوب ماذا يفعل",
                         "الصندوق المعدني للحاسوب", "كابل الطاقة", "شاشة العرض"],
             "correct": 0, "exp": "البرمجيات هي البرامج/التعليمات، والعتاد ينفّذها."},
            {"q": "ما هي وحدة المعالجة المركزية (CPU)؟",
             "options": ["عقل الحاسوب الذي يتحكّم ويعالج",
                         "جهاز لطباعة المستندات", "نوع من الذاكرة الخارجية", "مزوّد الطاقة للحاسوب"],
             "correct": 0, "exp": "المعالج هو عقل الحاسوب: يتحكّم ويعالج البيانات."},
            {"q": "ما هي الذاكرة العشوائية (RAM)؟",
             "options": ["ذاكرة رئيسية مؤقتة سريعة تفقد بياناتها عند انقطاع الكهرباء",
                         "تخزين دائم يحفظ البيانات للأبد", "جهاز إدخال", "متصفّح ويب"],
             "correct": 0, "exp": "الـRAM ذاكرة متطايرة: تُفقد محتوياتها عند انقطاع التيار."},
            {"q": "ما هو نظام التشغيل؟",
             "options": ["برمجية نظام تدير العتاد والموارد (مثل ويندوز)",
                         "تطبيق لتحرير الصور", "نوع من أجهزة الإدخال", "بروتوكول ويب"],
             "correct": 0, "exp": "نظام التشغيل برمجية نظام تشغّل الحاسوب وتدير موارده."},
            {"q": "ما هو الـ URL؟",
             "options": ["العنوان الكامل لصفحة الويب", "نوع من فيروسات الحاسوب",
                         "جهاز إخراج", "وحدة قياس للذاكرة"],
             "correct": 0, "exp": "الـURL هو العنوان الكامل لصفحة الويب."},
            {"q": "ما هو فيروس الحاسوب؟",
             "options": ["برنامج صغير ينتشر وقد يُتلف البيانات",
                         "أداة مفيدة تسرّع الحاسوب", "نوع من الشاشات", "نظام تشغيل رسمي"],
             "correct": 0, "exp": "الفيروس كود خبيث ينتشر وقد يُتلف أو يدمّر البيانات."},
            {"q": "ما هي ذاكرة الكاش (Cache)؟",
             "options": ["ذاكرة سريعة جداً قريبة من المعالج تسرّع الوصول",
                         "أكبر وأبطأ جهاز تخزين", "جهاز إدخال", "نوع من الطابعات"],
             "correct": 0, "exp": "الكاش ذاكرة صغيرة سريعة جداً قرب المعالج (L1, L2, L3)."},
            {"q": "ما هو الجدار الناري (Firewall)؟",
             "options": ["نظام يفحص حركة الشبكة ويمنع التهديدات",
                         "برنامج يصنع الفيروسات", "نوع من لوحات المفاتيح", "وحدة لقياس الذاكرة"],
             "correct": 0, "exp": "الجدار الناري يفحص المرور حسب قواعد ويمنع المخترقين والديدان."},
            {"q": "ما هي ذاكرة القراءة فقط (ROM)؟",
             "options": ["ذاكرة دائمة تخزّن تعليمات الإقلاع وتحتفظ ببياناتها بدون كهرباء",
                         "ذاكرة مؤقتة تفقد بياناتها عند فصل الكهرباء", "جهاز إدخال", "متصفّح ويب"],
             "correct": 0, "exp": "الـROM ذاكرة غير متطايرة؛ تحتفظ ببياناتها حتى بدون كهرباء."},
            {"q": "ما هو البت (Bit)؟",
             "options": ["أصغر وحدة بيانات، إما 0 أو 1", "مجموعة من 8 رموز",
                         "ألف بايت", "نوع من أجهزة الإدخال"],
             "correct": 0, "exp": "البت أصغر وحدة بيانات: 0 أو 1."},
            {"q": "ما هو البايت (Byte)؟",
             "options": ["مجموعة من 8 بتات", "رقم واحد 0 أو 1", "مليون بت", "جهاز إخراج"],
             "correct": 0, "exp": "1 بايت = 8 بت."},
            {"q": "ما هي وحدة الحساب والمنطق (ALU)؟",
             "options": ["جزء المعالج الذي ينفّذ العمليات الحسابية والمنطقية",
                         "جهاز التخزين الرئيسي", "نوع من الشاشات", "مزوّد الطاقة"],
             "correct": 0, "exp": "وحدة الحساب والمنطق تنفّذ العمليات الحسابية والمقارنات."},
            {"q": "ما هي وحدة التحكّم (CU)؟",
             "options": ["جزء المعالج الذي يوجّه وينسّق العمليات",
                         "ذاكرة تخزّن الملفات بشكل دائم", "جهاز إدخال", "كابل شبكة"],
             "correct": 0, "exp": "وحدة التحكّم توجّه عمليات المعالج وبقية الأجزاء."},
            {"q": "ما هو متصفّح الويب؟",
             "options": ["برنامج يُستخدم للوصول إلى صفحات الويب وعرضها",
                         "جهاز يطبع المستندات", "نوع من الذاكرة", "كابل إنترنت"],
             "correct": 0, "exp": "المتصفّح (مثل كروم) يتيح عرض صفحات الويب."},
            {"q": "ما هو الإنترنت؟",
             "options": ["شبكة عالمية تربط ملايين الحواسيب حول العالم",
                         "موقع واحد فقط", "نوع من الفيروسات", "جهاز إخراج"],
             "correct": 0, "exp": "الإنترنت هو الشبكة العالمية التي تربط الحواسيب."},
            {"q": "ما هي الشبكة العنكبوتية (WWW)؟",
             "options": ["خدمة من صفحات الويب المترابطة يتم الوصول إليها عبر الإنترنت",
                         "الكابلات المادية للإنترنت", "نوع من المعالجات", "جهاز تخزين"],
             "correct": 0, "exp": "الويب خدمة من صفحات مترابطة تعمل عبر الإنترنت."},
            {"q": "ما هو جهاز الإخراج؟",
             "options": ["جهاز يُخرج المعلومات من الحاسوب إلى المستخدم",
                         "جهاز يُدخل البيانات إلى الحاسوب", "جزء من المعالج", "نوع من الكابلات"],
             "correct": 0, "exp": "أجهزة الإخراج (الشاشة، الطابعة) توصّل النتائج للمستخدم."},
            {"q": "ما هي البرمجيات التطبيقية؟",
             "options": ["برامج تتيح للمستخدم إنجاز مهام محدّدة (مثل وورد وكروم)",
                         "برمجية تدير العتاد والموارد", "الأجزاء المادية للحاسوب", "نوع من الفيروسات"],
             "correct": 0, "exp": "البرمجيات التطبيقية تنفّذ مهام المستخدم المحدّدة."},
        ],
        "mcq": [
            {"q": "أيٌّ مما يلي جهاز إدخال؟",
             "options": ["لوحة المفاتيح", "الشاشة", "الطابعة", "السماعات"], "correct": 0,
             "exp": "لوحة المفاتيح ترسل البيانات إلى داخل الحاسوب، فهي جهاز إدخال."},
            {"q": "أيٌّ مما يلي جهاز إخراج؟",
             "options": ["الطابعة", "الفأرة", "الماسح الضوئي", "الميكروفون"], "correct": 0,
             "exp": "الطابعة تُخرج المعلومات للمستخدم، فهي جهاز إخراج."},
            {"q": "أي ناقل يحمل عناوين الذاكرة؟",
             "options": ["ناقل العناوين", "ناقل البيانات", "ناقل التحكّم", "ناقل USB"], "correct": 0,
             "exp": "ناقل العناوين يحمل موقع (عنوان) البيانات في الذاكرة."},
            {"q": "ما هي أصغر وحدة بيانات؟",
             "options": ["البت (Bit)", "البايت (Byte)", "الكيلوبايت", "الميغابايت"], "correct": 0,
             "exp": "البت (0 أو 1) أصغر وحدة، و8 بتات تساوي بايت واحد."},
            {"q": "البايت الواحد يساوي كم بت؟",
             "options": ["8 بت", "2 بت", "16 بت", "1024 بت"], "correct": 0, "exp": "1 بايت = 8 بت."},
            {"q": "أي جيل من الحواسيب استخدم الصمامات المفرّغة؟",
             "options": ["الجيل الأول", "الجيل الثالث", "الجيل الرابع", "الجيل الخامس"], "correct": 0,
             "exp": "الجيل الأول (1940-1956) استخدم الصمامات المفرّغة."},
            {"q": "أيٌّ مما يلي من برمجيات النظام؟",
             "options": ["ويندوز", "مايكروسوفت وورد", "جوجل كروم", "فوتوشوب"], "correct": 0,
             "exp": "ويندوز نظام تشغيل = برمجية نظام، والبقية تطبيقات."},
            {"q": "أي بروتوكول هو النسخة الآمنة للويب؟",
             "options": ["HTTPS", "HTTP", "FTP", "ISP"], "correct": 0,
             "exp": "الـHTTPS هو النسخة الآمنة المشفّرة من HTTP."},
            {"q": "أي برمجية خبيثة تتظاهر بأنها مفيدة وتُخفي أفعالاً ضارّة؟",
             "options": ["حصان طروادة", "برامج التجسّس", "برامج الإعلانات", "الديدان"], "correct": 0,
             "exp": "حصان طروادة يبدو نافعاً لكنه يُخفي أفعالاً ضارّة."},
            {"q": "رتّب من الأصغر إلى الأكبر:",
             "options": ["KB < MB < GB < TB", "TB < GB < MB < KB", "MB < KB < GB < TB", "GB < MB < TB < KB"],
             "correct": 0, "exp": "كيلوبايت < ميغابايت < غيغابايت < تيرابايت."},
            {"q": "أي ناقل يحمل البيانات الفعلية بين المعالج والذاكرة؟",
             "options": ["ناقل البيانات", "ناقل العناوين", "ناقل التحكّم", "ناقل الطاقة"], "correct": 0,
             "exp": "ناقل البيانات يحمل قيم البيانات الفعلية."},
            {"q": "أيٌّ مما يلي ليس جهاز إدخال؟",
             "options": ["الشاشة", "لوحة المفاتيح", "الفأرة", "الماسح الضوئي"], "correct": 0,
             "exp": "الشاشة جهاز إخراج وليست إدخالاً."},
            {"q": "أي ذاكرة متطايرة (تفقد بياناتها عند فصل الكهرباء)؟",
             "options": ["RAM", "ROM", "القرص الصلب", "SSD"], "correct": 0,
             "exp": "الـRAM متطايرة، والبقية تحتفظ بالبيانات بدون كهرباء."},
            {"q": "ما هي أكبر وحدة ذاكرة؟",
             "options": ["تيرابايت", "كيلوبايت", "ميغابايت", "غيغابايت"], "correct": 0,
             "exp": "التيرابايت الأكبر: KB < MB < GB < TB."},
            {"q": "أي جيل من الحواسيب استخدم الترانزستورات؟",
             "options": ["الجيل الثاني", "الجيل الأول", "الجيل الرابع", "الجيل الخامس"], "correct": 0,
             "exp": "الجيل الثاني استخدم الترانزستورات."},
            {"q": "أيٌّ مما يلي برمجية تطبيقية؟",
             "options": ["مايكروسوفت وورد", "ويندوز", "لينكس", "macOS"], "correct": 0,
             "exp": "وورد تطبيق، والبقية أنظمة تشغيل."},
            {"q": "أي بروتوكول يُستخدم لنقل الملفات؟",
             "options": ["FTP", "HTTP", "HTTPS", "ISP"], "correct": 0, "exp": "الـFTP بروتوكول نقل الملفات."},
            {"q": "أي برمجية خبيثة تجمع بياناتك وعاداتك في التصفّح سرّاً؟",
             "options": ["برامج التجسّس", "برامج الإعلانات", "الديدان", "الجدار الناري"], "correct": 0,
             "exp": "برامج التجسّس تجمع معلوماتك سرّاً."},
            {"q": "في الـURL، أي جزء هو 'https'؟",
             "options": ["البروتوكول", "اسم النطاق", "المسار", "حجم الملف"], "correct": 0,
             "exp": "الـ'https' هو جزء البروتوكول في العنوان."},
            {"q": "وحدة المعالجة المركزية تُعرف أيضاً باسم...؟",
             "options": ["المعالج (عقل الحاسوب)", "الشاشة", "مزوّد الطاقة", "القرص الصلب"], "correct": 0,
             "exp": "المعالج هو عقل الحاسوب."},
            {"q": "أي جهاز يعرض المخرجات بصرياً على شاشة؟",
             "options": ["الشاشة", "السماعة", "لوحة المفاتيح", "الميكروفون"], "correct": 0,
             "exp": "الشاشة تعرض المخرجات البصرية."},
            {"q": "كم عدد الوظائف الأساسية للحاسوب؟",
             "options": ["أربع (إدخال، معالجة، إخراج، تخزين)", "اثنتان", "ست", "ثلاث"], "correct": 0,
             "exp": "الإدخال والمعالجة والإخراج والتخزين = أربع وظائف."},
        ],
        "true_false": [
            {"q": "البرمجيات هي الجزء المادي من الحاسوب.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — البرمجيات هي البرامج، والجزء المادي هو العتاد."},
            {"q": "وحدة المعالجة المركزية تُسمّى عقل الحاسوب.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — المعالج يتحكّم ويعالج، مثل العقل."},
            {"q": "الذاكرة العشوائية (RAM) تحتفظ ببياناتها حتى عند فصل الكهرباء.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الـRAM متطايرة وتفقد بياناتها عند انقطاع التيار."},
            {"q": "HTTPS أكثر أماناً من HTTP.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — الـHTTPS هو النسخة المشفّرة الآمنة."},
            {"q": "الديدان (Worms) تحتاج تدخّلاً بشرياً لتنتشر.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الديدان تُفعّل نفسها وتنسخ ذاتها دون تدخّل بشري."},
            {"q": "الإنترنت والويب (WWW) هما الشيء نفسه تماماً.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الويب خدمة تعمل فوق الإنترنت."},
            {"q": "قرص الـSSD أسرع عموماً من القرص الصلب HDD.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — الـSSD بلا أجزاء متحرّكة وأسرع من الـHDD."},
            {"q": "الجدار الناري يساعد في منع المخترقين والديدان.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — الجدار الناري يفحص المرور ويمنع التهديدات."},
            {"q": "1 كيلوبايت أكبر من 1 ميغابايت.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الميغابايت أكبر؛ KB < MB < GB < TB."},
            {"q": "يجب تحديث برنامج مضاد الفيروسات باستمرار.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — التحديث يجعله يكشف أحدث التهديدات."},
            {"q": "ذاكرة ROM غير متطايرة (تحتفظ بالبيانات بدون كهرباء).",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — الـROM تحتفظ ببياناتها حتى عند فصل الكهرباء."},
            {"q": "الماسح الضوئي جهاز إخراج.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الماسح الضوئي جهاز إدخال."},
            {"q": "وحدة التحكّم تنفّذ العمليات الحسابية.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — وحدة الحساب والمنطق تنفّذ الحساب، ووحدة التحكّم توجّه."},
            {"q": "الميغابايت أكبر من الكيلوبايت.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — 1 ميغابايت = 1024 كيلوبايت."},
            {"q": "الجيل الأول من الحواسيب استخدم الترانزستورات.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الجيل الأول استخدم الصمامات المفرّغة."},
            {"q": "متصفّح الويب مثال على البرمجيات التطبيقية.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — المتصفّح برمجية تطبيقية."},
            {"q": "ناقل العناوين يحمل قيم البيانات الفعلية.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — ناقل العناوين يحمل العناوين، وناقل البيانات يحمل البيانات."},
            {"q": "برامج التجسّس تجمع معلومات المستخدم سرّاً.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — برامج التجسّس تجمع بياناتك خفية."},
            {"q": "HTTP أكثر أماناً من HTTPS.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الـHTTPS هو الآمن."},
            {"q": "ذاكرة الكاش أبطأ من الـRAM.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الكاش أسرع من الـRAM وأقرب للمعالج."},
            {"q": "الطابعة جهاز إدخال.",
             "options": ["صح", "خطأ"], "correct": 1, "exp": "خطأ — الطابعة جهاز إخراج."},
            {"q": "لوحة الأم تربط مكوّنات الحاسوب ببعضها.",
             "options": ["صح", "خطأ"], "correct": 0, "exp": "صح — لوحة الأم تربط جميع المكوّنات."},
        ],
    },
}


# ====================================================================
#  📝 امتحان الميد — أسئلة مقالية مع إجابات نموذجية
#  Mid Exam — open-ended questions with model answers
#  البنية: {"q": السؤال, "a": الإجابة النموذجية}
# ====================================================================
MID_EXAM = {
    "en": [
        {"q": "Define the computer and list its main components.",
         "a": ("A computer is an electronic device that receives data, processes it, "
               "and outputs it as useful information, and it can also store it.\n\n"
               "Its main components are:\n"
               "• Hardware — the physical parts: CPU, memory (RAM/ROM), "
               "input devices, output devices, and storage units.\n"
               "• Software — the programs and instructions that run the computer "
               "(system software + application software).")},
        {"q": "What are the functions of the computer?",
         "a": ("The computer has four basic functions:\n"
               "1) Input — receiving data from input devices.\n"
               "2) Processing — performing operations on the data using the CPU.\n"
               "3) Output — presenting the results to the user.\n"
               "4) Storage — saving data and information for later use.")},
        {"q": "List 5 input devices.",
         "a": ("Five input devices:\n"
               "1) Keyboard\n2) Mouse\n3) Scanner\n4) Camera\n5) Microphone\n"
               "(Also: Joystick / Touch screen.)")},
        {"q": "Define the motherboard and list its components.",
         "a": ("The motherboard is the main board that connects all the computer's "
               "components and lets them communicate with each other.\n\n"
               "Its key components are:\n"
               "• CPU socket\n• RAM (memory) slots\n• Chipset\n"
               "• Expansion slots (PCI / PCIe)\n• Storage ports (SATA)\n"
               "• I/O ports\n• BIOS / UEFI chip\n• Power connectors")},
        {"q": "List the main characteristics of the computer.",
         "a": ("• Speed — it processes data very fast.\n"
               "• Accuracy — its results are precise.\n"
               "• Storage — it can store huge amounts of data.\n"
               "• Diligence / Automation — it works without tiring and repeats tasks reliably.\n"
               "• Versatility — it can perform many different kinds of tasks.")},
        {"q": "List the output devices.",
         "a": ("Output devices send information out from the computer to the user:\n"
               "• Monitor (screen)\n• Printer\n• Speakers\n• Headphones\n• Projector")},
        {"q": "What is the difference between system software and application software?",
         "a": ("• System software (e.g. Windows, Linux) manages the hardware and runs "
               "the computer; it is essential.\n"
               "• Application software (e.g. Word, Chrome) is what the user runs to do "
               "specific tasks; it is optional and runs on top of the system software.")},
        {"q": "Define the CPU and mention its main parts.",
         "a": ("The CPU (Central Processing Unit) is the brain of the computer; it "
               "controls and processes data.\n\nIts main parts are:\n"
               "• ALU (Arithmetic Logic Unit) — performs calculations and comparisons.\n"
               "• Control Unit (CU) — directs and coordinates operations.\n"
               "• Registers — small, very fast temporary storage.")},
        {"q": "What is the difference between the Internet and the World Wide Web?",
         "a": ("• The Internet is the global network of connected computers — the "
               "infrastructure (cables, servers, devices).\n"
               "• The World Wide Web (WWW) is a service running on top of the Internet: "
               "a collection of linked web pages accessed through a browser.\n"
               "So the Web is one of the services that use the Internet.")},
        {"q": "List the common types of malware.",
         "a": ("• Spyware — secretly collects your data and browsing habits.\n"
               "• Adware — shows unwanted advertisements.\n"
               "• Trojan horse — looks useful but hides harmful actions.\n"
               "• Worms — self-replicate and spread across networks without human help.")},
    ],
    "ar": [
        {"q": "عرّف الحاسوب وما هي مكوناته؟",
         "a": ("الحاسوب جهاز إلكتروني يستقبل البيانات ويعالجها ويُخرجها على شكل معلومات "
               "مفيدة، ويستطيع أيضاً تخزينها.\n\n"
               "مكوناته الأساسية:\n"
               "• العتاد (Hardware) — الأجزاء المادية: وحدة المعالجة المركزية، الذاكرة "
               "(RAM/ROM)، أجهزة الإدخال، أجهزة الإخراج، ووحدات التخزين.\n"
               "• البرمجيات (Software) — البرامج والتعليمات التي تُشغّل الحاسوب "
               "(برمجيات النظام + البرمجيات التطبيقية).")},
        {"q": "ما هي وظائف الحاسوب؟",
         "a": ("وظائف الحاسوب الأساسية أربع:\n"
               "1) الإدخال (Input): استقبال البيانات من أجهزة الإدخال.\n"
               "2) المعالجة (Processing): تنفيذ العمليات على البيانات بواسطة المعالج.\n"
               "3) الإخراج (Output): عرض النتائج للمستخدم.\n"
               "4) التخزين (Storage): حفظ البيانات والمعلومات لاستخدامها لاحقاً.")},
        {"q": "عدّد 5 من أجهزة الإدخال.",
         "a": ("خمسة من أجهزة الإدخال:\n"
               "1) لوحة المفاتيح (Keyboard)\n2) الفأرة (Mouse)\n"
               "3) الماسح الضوئي (Scanner)\n4) الكاميرا (Camera)\n"
               "5) الميكروفون (Microphone)\n"
               "(ويمكن إضافة: عصا التحكّم Joystick / الشاشة اللمسية.)")},
        {"q": "عرّف لوحة الأم وما هي مكوناتها؟",
         "a": ("لوحة الأم (Motherboard) هي اللوحة الرئيسية التي تربط جميع مكوّنات الحاسوب "
               "وتتيح لها التواصل فيما بينها.\n\n"
               "أهم مكوناتها:\n"
               "• مقبس المعالج (CPU Socket)\n• فتحات الذاكرة (RAM Slots)\n"
               "• مجموعة الرقائق (Chipset)\n• فتحات التوسعة (PCI / PCIe)\n"
               "• منافذ التخزين (SATA)\n• منافذ الإدخال/الإخراج (I/O Ports)\n"
               "• رقاقة BIOS / UEFI\n• موصّلات الطاقة")},
        {"q": "اذكر خصائص الحاسوب الرئيسية.",
         "a": ("• السرعة: يعالج البيانات بسرعة عالية جداً.\n"
               "• الدقّة: نتائجه دقيقة.\n"
               "• التخزين: يخزّن كميات ضخمة من البيانات.\n"
               "• المثابرة/الأتمتة: يعمل دون كلل ويكرّر المهام بثبات.\n"
               "• تعدّد الاستخدامات: يؤدّي أنواعاً مختلفة كثيرة من المهام.")},
        {"q": "عدّد أجهزة الإخراج.",
         "a": ("أجهزة الإخراج تُخرج المعلومات من الحاسوب إلى المستخدم:\n"
               "• الشاشة (Monitor)\n• الطابعة (Printer)\n• السماعات (Speakers)\n"
               "• سماعات الرأس (Headphones)\n• جهاز العرض (Projector)")},
        {"q": "ما الفرق بين برمجيات النظام والبرمجيات التطبيقية؟",
         "a": ("• برمجيات النظام (مثل ويندوز ولينكس): تدير العتاد وتشغّل الحاسوب، وهي أساسية.\n"
               "• البرمجيات التطبيقية (مثل وورد وكروم): ما يشغّله المستخدم لإنجاز مهام "
               "محدّدة، وهي اختيارية وتعمل فوق برمجيات النظام.")},
        {"q": "عرّف وحدة المعالجة المركزية واذكر أجزاءها الرئيسية.",
         "a": ("وحدة المعالجة المركزية (CPU) هي عقل الحاسوب؛ تتحكّم وتعالج البيانات.\n\n"
               "أجزاؤها الرئيسية:\n"
               "• وحدة الحساب والمنطق (ALU): تنفّذ العمليات الحسابية والمقارنات.\n"
               "• وحدة التحكّم (CU): توجّه وتنسّق العمليات.\n"
               "• المسجّلات (Registers): تخزين مؤقت صغير وسريع جداً.")},
        {"q": "ما الفرق بين الإنترنت والشبكة العنكبوتية (الويب)؟",
         "a": ("• الإنترنت: الشبكة العالمية من الحواسيب المترابطة — البنية التحتية "
               "(كابلات، خوادم، أجهزة).\n"
               "• الويب (WWW): خدمة تعمل فوق الإنترنت — مجموعة من صفحات الويب المترابطة "
               "يتم الوصول إليها عبر المتصفّح.\n"
               "إذن الويب إحدى الخدمات التي تستخدم الإنترنت.")},
        {"q": "عدّد أنواع البرمجيات الخبيثة الشائعة.",
         "a": ("• برامج التجسّس (Spyware): تجمع بياناتك وعاداتك في التصفّح سرّاً.\n"
               "• برامج الإعلانات (Adware): تعرض إعلانات مزعجة.\n"
               "• حصان طروادة (Trojan): يبدو نافعاً لكنه يُخفي أفعالاً ضارّة.\n"
               "• الديدان (Worms): تنسخ نفسها وتنتشر عبر الشبكات دون تدخّل بشري.")},
    ],
}


def get_mid_exam(lang):
    """أسئلة امتحان الميد المقالية مخلوطة عشوائياً / Mid-exam open-ended questions, shuffled."""
    qs = list(MID_EXAM[lang])
    random.shuffle(qs)
    return qs


# تسميات الأقسام / Section labels (with transparent emoji icons)
CATEGORY_LABELS = {
    "en": {"definitions": "📖 Definitions", "mcq": "🔘 Multiple Choice", "true_false": "⚖️ True / False"},
    "ar": {"definitions": "📖 تعاريف", "mcq": "🔘 اختيارات", "true_false": "⚖️ صح وخطأ"},
}

CATEGORY_ORDER = ["definitions", "mcq", "true_false"]

# تسمية قسم امتحان الميد / Mid-exam section label
MIDEXAM_LABEL = {"ar": "📝 امتحان الميد", "en": "📝 Mid Exam"}


def get_questions(lang, category):
    """يرجع قائمة الأسئلة مخلوطة عشوائياً / Return shuffled question list for a language & category."""
    qs = list(QUESTIONS[lang][category])
    random.shuffle(qs)
    return qs


def get_full_test(lang):
    """الاختبار الشامل: كل الأسئلة من جميع الأقسام، مخلوطة عشوائياً / Comprehensive test: all questions, shuffled."""
    out = []
    for cat in CATEGORY_ORDER:
        out.extend(QUESTIONS[lang][cat])
    random.shuffle(out)
    return out
