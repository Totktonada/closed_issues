## Overview

The script to list issues closed on a week within a GitHub organization.

## Requirements

* Python 3.6+ (to support `%G` and `%V` in strptime());
* requests.

## How to use

Add a token on [Personal access token][gh_token] GitHub page, give
`repo:public_repo` access and copy the token to token.txt.

Run like so:

```sh
./closed_issues.py tarantool 17
```

The example of output:

```
metrics: [PR #2] RPM Spec
metrics: [PR #4] add collectors from stats
tarantool-c: [PR #129] travis-ci: update distros and repos & fix CentOS 6 build
tarantool: [#4174, 1.10.4] Add Ubuntu 19.04 Disco Dingo into CI
tarantool: [#4103, 2.2.0] sql: wrong type of addition string with integer
tarantool: [#4104, 2.2.0] Check access rights of table when accessing from VIEW
tarantool: [#4125, 2.1.3] tap: inconsistent work with box.NULL
tarantool: [#4157, 2.1.3] Segfault  (sql, transaction)
tarantool: [#3723, 2.2.0] sql: make predicates accept args only of type BOOL
tarantool: [#4126] sql: wrong type in meta in query with ORDER BY
tarantool: [#3942, 2.2.0] sql: repair mechanism for temporary registers
tarantool: [#4096, 1.10.4] 1.10.3: can't create tuple using :frommap() from map with an empty sequence key field
tarantool: [PR #4119] Add option for disable follow location behavior
tarantool: [#3106, 2.2.0] Make error message about 'delete by null' more informative
tarantool: [#3582, 1.10.4] primary index alter don't work on already unique fields
tarantool: [#4136] http.client: wrong error message
tarantool: [#4041, 1.10.4] Invalid index on update empty box.tuple
tarantool: [#3879, 2.2.0] sql: modify the signature of TRIM()
tarantool-java: [#86, JDBC MVP] jdbc: Support resultSetConcurrency parameter in Connection methods
ldecnumber: [#3] NaN rounding breaks further rounding calls
vshard: [#178, 0.2] Vshard storage reload nullifies bucket_ref_new
doc: [#760] Document new box.stat.net fields
doc: [#746] Poor "table" documentation
doc: [#747] box.stat.net.CONNECTIONS becomes a table
doc: [#756] new parameter for space before_replace and on_replace triggers
doc: [#759] Key match algorithm, provided in https://www.tarantool.io/en/doc/1.10/book/box/box_index/#box-index-index-pairs is incorrect
```

[gh_token]: https://github.com/settings/tokens
