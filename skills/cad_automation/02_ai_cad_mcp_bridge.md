# مهارة الأتمتة الهندسية 02: بروتوكول جسر الذكاء الاصطناعي مع الأوتوكاد (AI-to-CAD MCP Protocol)

> **الهدف:** توثيق قواعد وبروتوكول الاتصال المباشر بين نماذج الذكاء الاصطناعي (AI Agents) ومحرك الأوتوكاد (AutoCAD Engine) عبر بروتوكول سياق النموذج (Model Context Protocol - MCP) ومبادئ التحكم الآلي المستفادة من خوادم MCP المتخصصة.

---

## 1. فلسفة بروتوكول MCP في الأتمتة الهندسية

الهدف من جسر الـ MCP ليس مجرد إرسال أوامر نصية عشوائية، بل تحويل بيئة الـ CAD المعقدة إلى **مجموعة من الأدوات البرمجية القياسية (Tools)** القابلة للاستدعاء الدقيق بواسطة الوكيل الذكي:

```
[ Antigravity / AI Agent ]
         │
    (JSON-RPC / MCP Protocol)
         │
         ▼
[ CAD MCP Server (Bridge Engine) ]
   ├── Tool: query_entities (Layer, Bounds, Type)
   ├── Tool: get_block_attributes (Handle / Name)
   ├── Tool: insert_electrical_fixture (X, Y, Z, Block, Layer)
   ├── Tool: draw_circuit_conduit (Coordinates, Layer, Polyline)
   └── Tool: execute_cad_batch (Headless Accoreconsole)
         │
         ▼
[ AutoCAD Core / Active Session ]
```

---

## 2. القواعد الصارمة للتحكم الآلي عبر الذكاء الاصطناعي (Agent Directives)

### قاعدة 2.1: المعرف الدائم للكيان (The Entity Handle Rule)
- في أوتوكاد، لا يجوز للوكيل الذكي الاعتماد على إحداثيات العنصر فقط لتمييزه؛ فالإحداثيات قد تتشابه وتتغير.
- **المبدأ الإلزامي:** استخدام المقبض الدائم للكيان (`Entity Handle`) كمعرف فريد لا يتغير طوال حياة الملف.
- عند رغبة الوكيل في فحص، حصر، أو ربط كشاف ببريزة أو لوحة، يتم تسجيل الـ `Handle` الخاص بالرمز الكهربائي لربطه بجدول الكميات أو جدول الدوائر (Panel Schedule).

### قاعدة 2.2: الاستعلام النطاقي الموجه (Spatial & Layer Bounding Queries)
- ملفات الـ CAD تحتوي على مئات الآلاف من العناصر (Lines, Texts, Hatches).
- **يُحظر تماماً:** سحب كل كيانات الملف دفعة واحدة إلى سياق النموذج (Context Window Overflow).
- **البروتوكول الصحيح:**
  1. الاستعلام عبر **الصندوق المحيط (Bounding Box)** المحدد للفراغ أو الغرفة المعنية.
  2. فلترة الاستعلام بطبقات النظام فقط (مثال: `E-LGT-*` للإنارة، `E-PWR-*` للقوى).
  3. حصر نوع الكيانات المطلوبة (فقط `INSERT` للبلوكات أو `LWPOLYLINE` للمسارات).

### قاعدة 2.3: التعديل بالعمليات الذرية والـ Rollback (Atomic Execution)
- لا ينفذ الذكاء الاصطناعي أي تعديل في خطوة واحدة مفتوحة.
- يتم تجميع التعديلات في دفعة واحدة (Batch Transaction)؛ فإذا فشل إدراج رمز أو حدث تعارض هندسي، يتم التراجع الفوري (`Rollback`) دون ترك بقايا مشوهة في المخطط.

---

## 3. مجموعة أدوات MCP الموصى بها للأتمتة الكهربائية (MEP MCP Tool Suite)

عند بناء أو تكوين خادم MCP للأتمتة الكهربائية، يجب أن يشمل الأدوات الأساسية التالية:

| اسم الأداة (MCP Tool) | المدخلات (Parameters) | المخرجات الهندسية |
| :--- | :--- | :--- |
| `cad_get_drawing_matrix` | مسار الملف | استخراج شبكة المساقط (Floor Names, Grid Extents, System Coordinates). |
| `cad_count_blocks_in_bounds` | `min_pt, max_pt, layers, block_names` | حصر دقيق وفوري للرموز الهندسية داخل الغرفة أو الدور. |
| `cad_extract_panel_schedules` | `panel_layer, table_handle` | قراءة جداول اللوحات وسعات القواطع والأحمال من المخطط مباشرة. |
| `cad_measure_linear_runs` | `layer_pattern, bounds` | قياس أطوال الكابلات ومجاري الكابلات والمواسير مع تطبيق معاملات الارتفاع (3D Drops). |
| `cad_batch_insert_fixtures` | مصفوفة `{name, x, y, rot, layer, circuit}` | وضع الكشافات أو المخارج بعد حسابات التوزيع بضغطة واحدة. |

---

## 4. التكامل مع بيئة العمل المحلية (Local Stdio Transport)

- لتفادي الاعتماد على الإنترنت أو السيرفرات السحابية الخارجية لحماية بيانات المشاريع الحساسة:
- يتم تشغيل الـ MCP Server محلياً باستخدام `stdio` (Standard Input/Output) عبر بايثون أو .NET مباشرة على جهاز المهندس، مما يضمن أقصى سرعة تشغيل وأعلى مستوى من الخصوصية والسرية.
