
# MOEX Price API

Простое API, которое отдаёт текущую цену акции с Московской биржи (MOEX ISS).

## Пример запроса

```
GET /price?ticker=SBER
```

## Ответ

```json
{
  "ticker": "SBER",
  "price": 254.32
}
```
