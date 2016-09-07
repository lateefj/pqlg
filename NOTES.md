This load testing is to get a general idea of different things that impact performance. As a distributed system it can be complex to properly benchmark / load test however this should give guidance drastic differences in performance.

Run:

The typical run is 25 processes writing and 25 processes reading where each reader has 3 sub just for completeness (in a web scraper or other IO bound task this would be coroutines or threads).
| Concurrency | Jobs      | Inserts Per Second | Dequeue Per Second |
|-------------|:---------:|:------------------:|-------------------:|
| 25W/25R     | 250,000   | 1275.6833317788064 | 1287.2433412199268 |



Run with Gin Index:

```sql
CREATE INDEX queue_ids_idx ON queue USING GIN (q_name, (data #> '{ids}'::text[]));
```

| Concurrency | Jobs      | Inserts Per Second | Dequeue Per Second |
|-------------|:---------:|:------------------:|-------------------:|
| 25W/25R     | 250,000   | 314.6307633244511  | 316.26420818399646 |

