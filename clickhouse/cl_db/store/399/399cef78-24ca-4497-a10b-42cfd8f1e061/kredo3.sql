ATTACH TABLE _ UUID '101ebed1-f032-41cd-9a41-b5217c5a77aa'
(
    `id` Int32,
    `fname` String,
    `email` String,
    `time_def` DateTime64(3),
    `visual_ad2` Int32
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
