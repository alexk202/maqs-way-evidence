# ИСТОЧНИК МАТЕРИАЛОВ для поста r/LocalLLaMA — НЕ копировать в Reddit
# Reddit-автомоды банят ИИ-тексты и новичков. Путь: карма комментами (1-2 недели),
# затем пост СВОИМИ словами по фактам ниже (твои формулировки, мой план — копипаст убьет пост).

# План фактов для собственного текста:
# - личный заход: опиши СВОЮ память/подписку, где встречал «модель помнит не то»
# - ядро: фильтр ПОСЛЕ top-k = утечка/галлюцинация; фильтр ДО top-k = фикс (см. пермалинки ниже)
# - Graphiti-паттерн: противоречие сохраняет историю (expired_at), не удаляет
# - self-audit: один html-файл локально, 12 вопросов да/нет, output self-declared
# - вопросы сообществу в конце (вовлечение)
# - ссылки: 2-3 максимум, ниже готовые пермалинки

## Title (вариант для своего текста — переформулируй сам)
Context contamination in local AI memory is often a retrieval-order bug, not a model bug

## Факты и черновик (используй как материалы для СВОЕГО текста)

There's a bug class that looks like a "model hallucination problem" but is actually a retrieval-order bug, and I suspect plenty of local setups have it silently.

**The bug.** A vector store search applied the tenant filter AFTER the top-k retrieval. So when User B asked a question, the search first picked the nearest chunks from the whole index (including User A's memories), and only then tried to filter them by tenant — which dropped legit results and sometimes left User A's private memory visible to User B. From the outside it looks like your model is leaking or hallucinating. It's not the model. It's the retrieval order.

**The fix pattern (before top-k, not after).** We audited three open-source memory systems against our checklist (8 principles, written as verifiable properties) and one of them — Mem0 OSS — wires the isolation pattern right in code (our audit is static reading; nothing was run), worth copying:

- it REQUIRES a tenant filter (`user_id` / `agent_id` / `run_id`) on search — no filter, no query, it throws;
- the filter goes into the vector-store query BEFORE top-k;
- and it strips spoofable identity keys from user-supplied metadata, so you can't fake someone else's tenant id.

Code, pinned to the audited commit (so the link won't rot):
- tenant filter required: https://github.com/mem0ai/mem0/blob/0724291/mem0/memory/main.py#L1471-L1475
- filter before top-k: https://github.com/mem0ai/mem0/blob/0724291/mem0/vector_stores/qdrant.py#L428-L434
- anti-spoofing: https://github.com/mem0ai/mem0/blob/0724291/mem0/memory/main.py#L138-L162

A second pattern worth stealing — for stale memory instead of leaks: Graphiti (temporal knowledge graph) never DELETES old facts on contradiction. It keeps the old edge and marks it with `expired_at`, so history is preserved and "what did I believe back then" stays answerable:
https://github.com/getzep/graphiti/blob/aca3693/graphiti_core/edge_operations.py#L748-L781

**Self-audit, no cloud.** We packaged the checklist checks as a single static HTML file you can run locally against your own memory setup: it asks ~12 yes/no questions (is the tenant filter applied before top-k? is deleted memory still queryable? ...) and outputs a manifest you can keep. It's a self-report — honestly labeled "self-declared, not verified" in the output itself — but it takes 10 minutes and shows you which of the 8 principles you've never tested.

Checklist + audits (all reading-only, no ranking between the three systems, the point is the patterns, not a leaderboard):
- spec: https://github.com/alexk202/maqs-way/blob/main/SPEC.md
- the three worked audits: Mem0 / Graphiti / Letta — https://github.com/alexk202/maqs-way/tree/main/docs/audits

Question for you all: when you debug "the model remembers something wrong" in your local setups — do you check the retrieval order first, or the model? And has anyone else been bitten by filter-after-top-k?

---

## Пошагово (двухнедельный путь, не однодневный)

### Фаза 1: карма (сейчас, 1-2 недели)
1. Открой `https://www.reddit.com/r/LocalLLaMA/` — читай 30 мин/день.
2. Найди 3-5 тредов про память/контекст/агентов и оставь ПО-НАСТОЯЩЕМУ полезные комменты СВОИМИ словами (опыт с твоими локальными моделями — Qwen/Llama на 5060 Ti — это реальная ценность там).
3. Цель: ~50-100 кармы, ощущение языка саба. Без упоминаний проекта вообще.

### Фаза 2: пост (когда карма есть)
4. Пост пишешь сам по плану фактов выше (Title — свой вариант, Body — свои слова).
5. Вкладка **Post** → flair Discussion → Post.
6. Первые 2 часа: отвечай на комменты; признавать ошибки сразу; «no ranking» если начнется сравнение систем.
7. Ссылку на пост вписать в помеченное место в файле; пауза день; потом HN.

### Альтернатива (если карма-путь долог)
- **HN первым**: Show HN — единственная площадка, где свежий аккаунт автора проекта = норма, а не баг.
- **Комменты вместо постов**: можно вообще не постить — отвечать в чужих тредах о памяти по фактам из этого файла, со временем ссылки сами заживут.
4. **Title**: вставь строку из «## Title» выше (Ctrl+C / Ctrl+V).
5. **Text**: вставь весь блок из «## Body» выше — reddit сам поймет markdown (жирный, списки, ссылки).
6. Не ставь NSFW. Если reddit предложит выбрать flair — выбери **Discussion** (или оставь без flair, если Discussion нет).
7. Снизу справа **Post** — опубликовано.
8. Первые 2 часа: обновляй страницу, отвечай на комменты. Правила ответов: благодарить за конкретику, признавать ошибки сразу («you're right, we'll fix the pointer»), НЕ спорить про «чей memory лучше» — отсылай «no ranking, the point is the patterns».
9. Если пост заминусили без обсуждения — не перезаливай в тот же день. Пауза день, потом решай с советом.

## После (дисциплина)
- Ссылку на созданный пост сохрани в эту заметку: [ЗАПОЛНИТЬ ПОСЛЕ ПУБЛИКАЦИИ]
- Пауза минимум день до следующей площадки (HN).
- Правки текста ПОСЛЕ публикации — только дописыванием в комменты (reddit-этикет), не редактированием тела.

## Отчет совету (после публикации)
Пришли сюда: ссылку на пост + 2-3 лучших коммента + свои выводы. Дальше — HN по его разделу в drafts.md (там Title уже готов).
