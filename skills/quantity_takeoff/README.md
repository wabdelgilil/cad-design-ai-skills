# Master MEP Quantity Takeoff & Estimation Skills Library
## دستور ومنهجية مهندس الحصر والتصميم (MEP BOQ & Cost Engineering Constitution)

هذه الحزمة تؤسس البنية التحتية القياسية لحصر كميات وتكاليف الأعمال الكهروميكانيكية (MEP: صحي، ميكانيكي، كهربائي) من واقع الخبرة الهندسية الميدانية والاستشارية العميقة. تهدف إلى تحويل عملية الحصر من مجرد "عد وتخمين أعمى" إلى **علم هندسي دقيق قابل للتنفيذ والتدقيق والربط المالي الصارم**.

---

## هيكلية حزمة مهارات الحصر (Skills Architecture)

| الرمز الكودي | الوثيقة الهندسية | النطاق والمحتوى الهندسي | الهدف والنتيجة |
| :--- | :--- | :--- | :--- |
| **SKILL-QTO-01** | [`01_fundamental_pillars.md`](file:///d:/programming/ElectricalDesign/core/skills/quantity_takeoff/01_fundamental_pillars.md) | **القواعد الأساسية الست (The 6 Fundamental Pillars):**<br>1. قاعدة الرؤية المجسمة ثلاثية الأبعاد (3D Reality).<br>2. قاعدة مصفوفة الفراغات المعمارية (Spatial Audit).<br>3. قاعدة المنظومة المتكاملة للمخرج (Fixture Ecosystem).<br>4. قاعدة التقدير المشتق لقطع الوصل (Derived Fittings).<br>5. قاعدة الفصل بين الصافي والتوريد (Net vs Procurement).<br>6. قاعدة المصدر الموحد وقابلية التتبع (Traceability). | منع أي سقطات كارثية في الحصر، كشف النواقص في الصواعد والهوابط، وتأصيل الدقة بنسبة 100%. |
| **SKILL-QTO-02** | [`02_sub_rules_and_heuristics.md`](file:///d:/programming/ElectricalDesign/core/skills/quantity_takeoff/02_sub_rules_and_heuristics.md) | **القواعد الفرعية والنسب الحسابية الدقيقة:**<br>- معادلات الهوابط الرأسية الجدارية للأجهزة.<br>- شجرة الإكسسوارات المخفية لكل مخرج صحي وكهربائي.<br>- نسب ومعادلات قطع الوصل ومستلزمات التثبيت للأنابيب.<br>- جداول نسب الهالك المعتمدة حسب طبيعة المادة. | تمكين الوكيل والمهندس من استنتاج كافة المستلزمات المخفية رياضياً بدقة متناهية دون إغفال أي قطعة. |
| **SKILL-QTO-03** | [`03_boq_data_structure_and_templates.md`](file:///d:/programming/ElectricalDesign/core/skills/quantity_takeoff/03_boq_data_structure_and_templates.md) | **البنية التحتية لملفات الإكسل وقوالب جداول الكميات:**<br>- معمارية التبويبات الخمسة القياسية.<br>- هندسة المعادلات الديناميكية وحظر الأرقام الصامتة (Hardcoded Values).<br>- قواعد التنسيق البصري الاحترافي ونظام RTL.<br>- كود بايثون المعياري لتوليد جداول الكميات. | توحيد شكل ومخرجات جداول الكميات لتكون جاهزة للمناقصات والاعتماد الاستشاري فوراً. |

---

## التكامل مع النواة البرمجية (Core Integration)

تتكامل هذه المهارات مباشرة مع:
* بنك الذاكرة التراكمي: [`core/memory/domain_heuristics.json`](file:///d:/programming/ElectricalDesign/core/memory/domain_heuristics.json)
* حيل وسكربتات المعالجة: [`core/memory/scripting_tricks.json`](file:///d:/programming/ElectricalDesign/core/memory/scripting_tricks.json)
* سكربتات حصر المشاريع: `projects/[PROJECT_NAME]/scripts/`
