DROP DATABASE IF EXISTS music_tm;
CREATE DATABASE music_tm;

USE music_tm;


CREATE TABLE `users` (
    `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `email` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `active` tinyint(1) DEFAULT 1,
    `rank` int(11) DEFAULT 0,
    `role` varchar(50) COLLATE utf8_unicode_ci DEFAULT 'all',
    `date_created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `date_updated` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


-- CREATE TABLE `user_roles` (
--     `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
--     `role` varchar(50) COLLATE utf8_unicode_ci DEFAULT 'all',
--     PRIMARY KEY (`user_id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `user_scopes` (
    `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `mida` varchar(50) COLLATE utf8_unicode_ci,
    `scope` varchar(200) COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `session` (
    `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `mida` varchar(50) COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `scopes` (
    `scope` varchar(20) COLLATE utf8_unicode_ci,
    `description` varchar(200) COLLATE utf8_unicode_ci,
    `roles` varchar(50) COLLATE utf8_unicode_ci,
    PRIMARY KEY (`scope`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `music_providers` (
    `id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `name` varchar(50) COLLATE utf8_unicode_ci,
    `description` varchar(200) COLLATE utf8_unicode_ci,
    `logo` varchar(100) COLLATE utf8_unicode_ci,
    `banner` varchar(100) COLLATE utf8_unicode_ci,
    `website` varchar(100) COLLATE utf8_unicode_ci,
    `owner_id` varchar(37) COLLATE utf8_unicode_ci,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `music_provider_managers` (
    `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `mp_id` varchar(37) COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `tracks` (
    `track_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
    `title` varchar(1000) COLLATE utf8_unicode_ci,
    `artist` varchar(1000) COLLATE utf8_unicode_ci,
    `album` varchar(1000) COLLATE utf8_unicode_ci,
    `genre` varchar(1000) COLLATE utf8_unicode_ci,
    `mood` varchar(1000) COLLATE utf8_unicode_ci,
    `instrument` varchar(1000) COLLATE utf8_unicode_ci,
    `lyrics` text(1000000) COLLATE utf8_unicode_ci,
    `country` varchar(50) COLLATE utf8_unicode_ci,
    `filename` varchar(50) COLLATE utf8_unicode_ci,
    PRIMARY KEY (`track_id`),
    INDEX `titles` (`title`(10)),
    INDEX `artists` (`artist`(10)),
    INDEX `albums` (`album`(10)),
    INDEX `countries` (`country`(10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


-- CREATE TABLE `users_access_token` (
--     `user_id` varchar(37) COLLATE utf8_unicode_ci NOT NULL,
--     `access_token` varchar(37) COLLATE utf8_unicode_ci DEFAULT NULL,
--     `access_token_expiry` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
--     `refresh_token` datetime DEFAULT NULL,
--     PRIMARY KEY (`user_id`)
-- );
