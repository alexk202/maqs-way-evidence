# HN answer bank — Show HN retry (drafts only, do not auto-post)

Cycle: draft → review → правки → sanction → send вручную. Ничего отсюда не постится автоматически.
Account: восстановленный `aleks202` (второй аккаунт = evasion = перманент). План: вт 20.10, ~15:00–17:00 МСК.
Posting language: English. Готовые блоки «A:» — HN-safe, копируй как есть (минимум правок).

## Правила форматирования HN (иначе flagged, как первый тред)
- Пустая строка между КАЖДЫМ абзацем. Одиночный перенос слипает строки.
- Никаких `**звёздочек**`, никаких markdown-заголовков — рендерятся литерально.
- НЕ начинай строку с пробелов/`-`/цифры+точки — отступ = preformatted-блок. Пиши прозой.
- Ссылки голым URL — HN сам делает их кликабельными.
- Первый коммент = disclosure "I'm the author." (уже в hn-post.md).

## Три железных правила (нарушение = kill)
1. Никогда не просить апвоты/шеринг.
2. Никакого ранжирования Mem0/Graphiti/Letta — только «different scopes, no ranking».
3. Ноль удалений: правка на месте ≤~2ч; формат-ошибку гаси своим вторым комментом.

---

## A. Прямые вызовы методологии

### A1. «Это просто чтение кода, ты ничего не запускал. Это не evidence.»
A: Static reading is the honest claim, not a hidden one. I verify code paths by construction, not by execution, and I state that boundary in the post. What makes it checkable: every finding is pinned to a commit and a file:line you can open right now, and the audit ships an executable replay of the eight declared negative vectors so the gate fails where it should. If I misread a pointer, the wrong pointer gets fixed and a genuine misread gets the finding withdrawn in a second commit.

### A2. «Дай мне самому проверить, а не верь тебе.»
A: That is the point. The evaluator is a single index.html with zero dependencies — open it, run it against your own manifest locally, no setup, no cloud. It stamps the output self-declared, not verified, and every check carries the exact command to verify it yourself. The gate itself replays the canon: schema, manifest, namespaces, a canon pin, and the eight negative vectors, never merged into one pass/fail.

### A3. «Ваш self-audit ничего не стоит — это самооценка.»
A: Agreed, which is why it is labeled self-declared and never presented as proof. Two things keep it honest: the manifest is only an input, and the gate recomputes coverage independently, including an executable replay of the negative vectors where a miss is a miss. Self-declaration is a starting form, not the verdict.

### A4. «Кто это писал — LLM?»
A: The checklist and the audits are mine. Tooling helped draft wording, but the artifact is not the prose: every claim is a pointer to a pinned commit and file:line, and each one is either right or wrong against the code. Check any line and you judge the artifact, not me. [OWNER: подправить формулировку под факт, как было на самом деле]
<!-- Если использовался ИИ — сказать честно и коротко, не оправдываться. Falsifiability отвечает за качество, а не происхождение. -->

## B. Цифры и статистика

### B1. «R@5 0.98 на n=50 — это же ничего. Где второй прогон?»
A: Correct, and that is exactly how I present it: one pre-registered measurement, single point, not a normative threshold. After the post I ran the full 500: evidence-R@5 = 0.992 (496/500), Wilson [0.980,0.997], within the pre-registered [0.90,1.00]. The point of pre-registration was to fix the number before seeing it; the gates stay per-deployment candidates, not claims.

### B2. «Откуда взялись пороги 0.7/0.85 и остальные?» (§3.2)
A: They are candidates, not laws. The 0.7/0.85 recall, 0.65/0.8 temporal, 0.8/0.9 abstention set is the normative table SPEC section 3.2 proposes; my job in this post was to argue with numbers whether they are realistic per deployment. One pre-registered run does not settle a threshold — it starts the argument. Tell me where you would set them and why.

### B3. «Что такое oracle haystack? Почему oracle — это читерство?»
A: Oracle haystack means the correct evidence is guaranteed present, so it isolates retrieval ranking from ingestion. It is deliberately the easiest setting: if a system cannot hit R@5 with the answer guaranteed in the store, that is a clean retrieval failure, not an ingestion one. It is a floor, not a field benchmark, and I label it that way.

### B4. «Слабые промахи на full-500 — что это было?»
A: All failures concentrated on the extraction side: truncated JSON near the max_tokens ceiling, not a ranking defect. On the single-156 slice, raising the cap from 1200 to 2000 cut the length-share of failures from 2.6% to 1.3% — roughly half, not zero — and about 1.3% malformed output persisted, so a bigger token cap does not fully fix it. I withdrew a masking hypothesis on this data because its premise did not survive; a summarization defect remains open.

### B5. «Wilson-интервал при n=500 узкий — покажи предпосылки.»
A: Fair. It is a binomial Wilson interval over 500 independent items, [0.980,0.997] at 0.992. The honest caveat is dependence: items share one model and one ingestion path, so treat it as a within-set interval, not a population estimate. It is reported as uncertainty of this run, not of the method in general.

## C. Вендоры, сравнения, ранжирование

### C1. «Ты ранжируешь Mem0/Graphiti/Letta? Кто лучше?»
A: No ranking, and the scopes are not the same, so a ranking would be fake precision. Mem0 OSS: tenant isolation reads right in code (static evidence, behavioral run pending), weaker on deletion tombstones. Graphiti: contradiction handling reads right in code (same status), weaker on default scoping. Letta: fail-closed by construction in the client scope only; the server is closed source and unjudged. Different designs, different boundaries.

### C2. «Ты вообще связывался с командами?»
A: Yes, before posting. Mem0 and Letta were contacted directly, and the Graphiti contact is public: https://github.com/alexk202/maqs-way/issues/3 — an open invitation in their tracker. I do not put words in their mouths; the repo is the door.

### C3. «Это выглядит как публичный разнос Mem0/Graphiti/Letta ради трафика.»
A: The intent is the opposite: each audit leads with what the system gets right, and the gaps are the same category of thing I list against my own spec. The worked patterns on the repo are copy-the-good-part guides, not takedowns. If a finding is wrong, it gets withdrawn in a commit.

### C4. «Почему Mem0, а не [ваш любимый проект]?»
A: Because they are the three most-adopted open memory layers and they are auditable — code I can pin to a commit and read. The checklist is vendor-neutral: it applies to your system the same way, and I would welcome a fourth audit as a PR.

## D. Понятия и канон

### D1. «MAQS vs Way — в чём разница?»
A: One line: MAQS audits that a mechanism exists; Way proves it works. MAQS is the static audit core (v1.6). Way is the layer that makes it falsifiable — declared vectors get replayed, and a metric has to move, not just a checkbox.

### D2. «Что именно запускает `maqs_way_audit.py all`?»
A: One command replays: schema 4/4, manifest 12/12, namespace checks, a canon pin (similarity 0.3 against SPEC section 3.3), an executable replay of all eight declared negative vectors reported as caught/missed/error and never merged, and a 24-row scoreboard of every audit claim. It ends on a single gate verdict, not a pile of green checkmarks.

### D3. «Что такое детектор RED-ветки?»
A: The gate has to fail where it should. The repo ships three negative branches — orphan, pin-drift, dangling-owner — wired into run_all.sh, and the pipeline only exits 0 if the detector goes RED on all three and GREEN on the clean tree. A gate that can never fail is decoration.

### D4. «Почему вы называете это falsifiable, а не empirical?»
A: Falsifiable is the narrow, checkable claim: every assertion carries a commit and a file:line, so anyone can falsify it by opening the code, and misreads get a second commit. Empirical would require execution-based evidence at scale, which I explicitly do not yet claim — that is what the one measured run is, a start.

## E. Открытые пробелы, процесс, вклад

### E1. «Двенадцать гапов, все "retargeted to v0.3" — это же пар vaporware.»
A: The rule is a release may carry gaps, never silent gaps: each gap has an id, an owner, and a closes_in, and a moved one carries a retarget note so nothing rolls over quietly. B4 is multi-store atomicity; E10/E11 are assembly rules pending canonization; I10–I15 are logging and drift rules. They are listed in the open, which is the opposite of hiding them until later.

### E2. «Почему у гапов owner — исторический, а не резолвящийся?»
A: Because honesty beats false green. The full v0.2 gap list is a reference with history labels, not gate-resolvable owners, and it is explicitly marked template-not-canon so it is never fed to coverage gates. Gate-resolvable ownership is the per-repo template.

### E3. «Можно ли это внедрить у себя / принять PR?»
A: Yes, that is the ask. Copy the GitHub Action template or the gaps template into your repo, run the checklist, and tell me what does not fit — telling me what does not fit is as useful as what does. RFC skeleton is in the repo; a fourth audit or a threshold correction is a welcome PR.

### E4. «Зачем ещё один чек-лист? Уже есть LongMemEval / LoCoMo.»
A: Those measure a system; this makes a system's design claims checkable before you run it — does the tenant filter apply before top-k, does contradiction expire or delete, is deletion tombstoned. Benchmarks and this are complements: one scores outcomes, the other pins the code paths that produce them. If a benchmark already covers a check, say so and I retarget.

### E5. «Это форк/копия чужого кода?»
A: No. The audits are static readings of pinned upstream commits with file:line, and the copy-the-good-part notes are short derived guides. Canon logic is never duplicated here; this repo derives from canon and waits for owner signature on anything upstream. [OWNER: подтвердить лицензию/атрибуцию перед постом]

## F. Хост-режим (троллинг / не по теме)

- Никогда не флагать в ответ на критику. Троллинг игнорируй: молчание — валидный ответ.
- Отвечай только на содержательное: конкретный file:line, конкретная цифра, конкретная ошибка методологии.
- «Show HN» требует быть готовым к «this is just a README» — ответ A1/A2/A3, один раз, без повторов и без спора о тоне.
- Похвала без вопроса → короткое «thanks», не растекаться.

## G. Правило «не знаю»

Если на вопрос нет факта под рукой: не выдумывать. Шаблон:
A: I do not want to answer from memory and get it wrong. Let me check the code/spec and come back with the exact pointer.
Потом реально вернуться с file:line. Это сильнее, чем уверенный неверный ответ.

## H. Коррекция (сильнейший ход)

Если указали на реальную ошибку в file:line:
A: You're right — that pointer is wrong. Fixed in a second commit: [commit URL]. The finding stands/withdraws accordingly.
Затем РЕАЛЬНО сделать коммит в canon/audit и вставить URL. Слово, подтверждённое делом.
Если указали на ошибку, которой нет — спокойно показать строку, не спорить о тоне.

---

## После публикации
- Ссылку на тред вписать в `outreach/hn-post.md` (поле после публикации).
- Лучшие вопросы + свои ответы скинуть в совет — вычистим формулировки.
- Пауза сутки, потом LocalLLaMA по karma-phase (`outreach/locallama-post.md`), затем Discussions.
