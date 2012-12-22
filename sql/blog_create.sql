BEGIN;
CREATE TABLE "webblog_category" (
    "category_id" integer NOT NULL PRIMARY KEY,
    "name" varchar(20) NOT NULL,
    "create_time" datetime NOT NULL,
    "category_rate" smallint NOT NULL
)
;
CREATE TABLE "blog" (
    "blog_id" integer NOT NULL PRIMARY KEY,
    "category_id_id" integer NOT NULL REFERENCES "webblog_category" ("category_id"),
    "title" varchar(20) NOT NULL UNIQUE,
    "desc" varchar(150) NOT NULL,
    "content" text NOT NULL,
    "pub_time" datetime NOT NULL,
    "update_time" datetime NOT NULL,
    "is_pub" smallint NOT NULL,
    "is_close" smallint NOT NULL,
    "is_visiable" smallint NOT NULL
)
;
CREATE TABLE "webblog_tag" (
    "tag_id" integer NOT NULL PRIMARY KEY,
    "tag_name" varchar(20) NOT NULL UNIQUE,
    "desc" varchar(50) NOT NULL,
    "create_time" date NOT NULL,
    "tag_rate" smallint NOT NULL
)
;
CREATE TABLE "webblog_blog_tag" (
    "blog_id_id" integer NOT NULL PRIMARY KEY REFERENCES "blog" ("blog_id"),
    "Tag_id_id" integer NOT NULL PRIMARY KEY REFERENCES "webblog_tag" ("tag_id")
)
;
CREATE TABLE "webblog_comment" (
    "comment_id" integer NOT NULL PRIMARY KEY,
    "author_name" varchar(10) NOT NULL,
    "author_email" varchar(75) NOT NULL,
    "content" text NOT NULL,
    "is_close" smallint NOT NULL,
    "is_discard" smallint NOT NULL,
    "comment_level" smallint NOT NULL,
    "parent_id_id" integer NOT NULL,
    "blog_id_id" integer NOT NULL REFERENCES "blog" ("blog_id")
)
;
CREATE INDEX "blog_56c2042b" ON "blog" ("category_id_id");
CREATE INDEX "blog_646331b4" ON "blog" ("pub_time");
CREATE INDEX "webblog_comment_1cf7ee57" ON "webblog_comment" ("parent_id_id");
CREATE INDEX "webblog_comment_301daeed" ON "webblog_comment" ("blog_id_id");
COMMIT;
