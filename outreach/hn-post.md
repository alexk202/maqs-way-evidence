# HN ПАКЕТ — Show HN (готово к использованию)

# ВАЖНО: HN — не ИИ-текст-бан, а культура "author = ок".
# Show HN от автора проекта с новым аккаунтом — норма там. Но:
# - Title только свой, без маркетинговых суперлативов
# - НИКОГДА не просить апвоты (мгновенный kill)
# - Первый коммент = disclosure "I'm the author" — обязательный этикет
#
# ПЕРЕСОЗДАНИЕ ТРЕДА = СМЕРТЬ АККАУНТА (урок 17.10, аккаунт aleks202):
# delete + resubmit антиспам читает как спам-паттерн и режет право постить.
# ЕСЛИ ПОСТ НЕ УДАЛСЯ:
#   1) НЕ удалять сабмит. Edit доступен ~2 часа — правь титул/коммент на месте.
#   2) Формат-ошибка в комменте → ответь своим вторым комментом с исправлением.
#   3) Аккаунт уже убит → письмо hn@ycombinator.com (ПРАВИЛЬНЫЙ адрес — contact
#      внизу любой страницы HN; dang читает именно его. Честно: что случилось,
#      что понял, просьба восстановить + username; 1 письмо, ответ 1-3 дня;
#      НИКОГДА не создавать второй аккаунт — это evasion = перманент).

## Шаг 1 — Title (лимит HN 80 символов; 62 — влезает)
Show HN: MAQS-Way – falsifiable audits of AI memory frameworks

# урок первой попытки: длинный вариант (91 символ) не прошел; деталь
# "every claim with file:line" переехала в первый коммент — там она и есть

## Шаг 2 — URL (в поле url)
https://github.com/alexk202/maqs-way

## Шаг 3 — текст: НЕ в post (link-пост тела не имеет!), а ПЕРВЫМ КОММЕНТОМ

# ФОРМАТИРОВАНИЕ HN (урок первой попытки, тред был flagged за markdown-стену):
# - **жирный** НЕ работает — рендерится literally, выглядит спамом
# - одиночный перенос НЕ работает — строки слипаются в один абзац
# - ПРАВИЛО: между КАЖДЫМ пунктом пустая строка, никаких звездочек вообще

HN-БЕЗОПАСНЫЙ текст (копируй как есть):

---
I'm the author. I audited three open-source memory systems (Mem0, Graphiti, Letta) against a memory-quality checklist I maintain, and shipped the checklist plus the audits as one repo.

Static code reading, every claim pinned to a commit and file:line so links can't rot and claims are falsifiable.

Mem0 OSS: tenant isolation done right. A tenant filter is required on every search and applied BEFORE top-k, identity keys are stripped from user metadata so tenants can't be spoofed. Weaker side: deleted memories stay queryable through the history table, no tombstone.

Graphiti: contradiction handling is exemplary. Old edges are retained with expired_at instead of deleted, so "what did I believe back then" stays answerable. Weaker side: unscoped search is allowed by default.

Letta (MemFS client scope only): fail-closed by construction. Per-agent roots, symlink-resolved containment, default-deny writes. Server side is closed source and unjudged.

How the checks run: one command (maqs_way_audit.py all) replays schema 4/4 + manifest 12/12 + namespaces + a canon pin (similarity 0.3 vs SPEC section 3.3) + an executable replay of all 8 declared negative vectors (caught/missed/error, never merged) + a 24-row scoreboard of every audit claim.

Known gaps are listed openly: B4 multi-store atomicity, E10/E11 and I10-I15 pending canonization, all retargeted to v0.3. A release may carry gaps, never silent gaps.

I contacted all three teams before posting. Worked example of the Graphiti contact: https://github.com/alexk202/maqs-way/issues/3

Honest boundary: static reading verifies code paths by construction, not by execution. If we misread anything, the wrong pointer gets fixed and a genuine misread gets the finding withdrawn; corrections land as a second commit.

Ask: what would make this checklist worth adopting outside our own projects? Feedback on the thresholds table (SPEC section 3.2) especially welcome.

## Шаг 4 — когда постить
Лучшее окно: вторник-четверг, утро США = 15:00-17:00 по Москве/ЕКБ. Худшее: ночь и выходные (утонет).

## Шаг 5 — клики
1. https://news.ycombinator.com/login → войди/создай аккаунт (1 минута, email не обязателен).
2. Верхнее меню → **submit**.
3. title → вставь из Шага 1. url → вставь из Шага 2. Поле text оставь ПУСТЫМ.
4. **submit** → сразу же открой свой пост → внизу textarea → вставь первый коммент из Шага 3 → **add comment**.

## Шаг 6 — правила выживания в треде
- Отвечай на содержательную критику, троллинг игнорируй (не флагай).
- Если указали на ошибку в file:line — «you're right, fixing the pointer» + реальный второй коммит в repo. Это сильнейший ход: слово, подтвержденное делом.
- Про Mem0/Graphiti/Letta — только «no ranking», сравнения не начинай.
- Просить апвоты/делиться с друзьями = insta-kill. Никому не ссылайся на тред вне контекста.

## После
- Ссылка на пост: [ЗАПОЛНИТЬ ПОСЛЕ ПУБЛИКАЦИИ]
- Пауза сутки. Потом — LocalLLaMA по карма-фазе (файл locallama-post.md) и Discussions.

## Отчет совету
Скинь сюда ссылку треда + лучшие вопросы — помогу готовить ответы.
