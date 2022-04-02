## Django

```
                                     Table "public.django_migrations"
 Column  |           Type           | Collation | Nullable |                    Default                    
---------+--------------------------+-----------+----------+-----------------------------------------------
 id      | bigint                   |           | not null | nextval('django_migrations_id_seq'::regclass)
 app     | character varying(255)   |           | not null | 
 name    | character varying(255)   |           | not null | 
 applied | timestamp with time zone |           | not null | 
Indexes:
    "django_migrations_pkey" PRIMARY KEY, btree (id)
```

```
 id |     app      |                   name                   |            applied            
----+--------------+------------------------------------------+-------------------------------
  1 | contenttypes | 0001_initial                             | 2022-04-02 05:41:57.808182+00
  2 | auth         | 0001_initial                             | 2022-04-02 05:41:59.300608+00
  3 | admin        | 0001_initial                             | 2022-04-02 05:41:59.550758+00
  4 | admin        | 0002_logentry_remove_auto_add            | 2022-04-02 05:41:59.573025+00
  5 | admin        | 0003_logentry_add_action_flag_choices    | 2022-04-02 05:41:59.600354+00
  6 | contenttypes | 0002_remove_content_type_name            | 2022-04-02 05:41:59.696596+00
  7 | auth         | 0002_alter_permission_name_max_length    | 2022-04-02 05:41:59.71988+00
  8 | auth         | 0003_alter_user_email_max_length         | 2022-04-02 05:41:59.746759+00
  9 | auth         | 0004_alter_user_username_opts            | 2022-04-02 05:41:59.769603+00
 10 | auth         | 0005_alter_user_last_login_null          | 2022-04-02 05:41:59.79967+00
 11 | auth         | 0006_require_contenttypes_0002           | 2022-04-02 05:41:59.80967+00
 12 | auth         | 0007_alter_validators_add_error_messages | 2022-04-02 05:41:59.829089+00
 13 | auth         | 0008_alter_user_username_max_length      | 2022-04-02 05:41:59.922161+00
 14 | auth         | 0009_alter_user_last_name_max_length     | 2022-04-02 05:41:59.953669+00
 15 | auth         | 0010_alter_group_name_max_length         | 2022-04-02 05:41:59.976697+00
 16 | auth         | 0011_update_proxy_permissions            | 2022-04-02 05:42:00.000545+00
 17 | auth         | 0012_alter_user_first_name_max_length    | 2022-04-02 05:42:00.027668+00
 18 | sessions     | 0001_initial                             | 2022-04-02 05:42:00.261356+00
 19 | app          | 0001_initial                             | 2022-04-02 06:12:05.903575+00
 20 | app          | 0002_alter_user_email                    | 2022-04-02 12:56:33.117165+00
```

## Laravel
```
                                     Table "public.migrations"
  Column   |          Type          | Collation | Nullable |                Default                 
-----------+------------------------+-----------+----------+----------------------------------------
 id        | integer                |           | not null | nextval('migrations_id_seq'::regclass)
 migration | character varying(255) |           | not null | 
 batch     | integer                |           | not null | 
Indexes:
    "migrations_pkey" PRIMARY KEY, btree (id)
```

```
 id |                       migration                       | batch 
----+-------------------------------------------------------+-------
  1 | 2014_10_12_000000_create_users_table                  |     1
  2 | 2014_10_12_100000_create_password_resets_table        |     1
  3 | 2019_08_19_000000_create_failed_jobs_table            |     1
  4 | 2019_12_14_000001_create_personal_access_tokens_table |     1
  5 | 2022_04_02_184216_aaa                                 |     2
```
batchは何回目のマイグレーションで実行したか。同じ数字は同じタイミングで実行されたことを表す。
