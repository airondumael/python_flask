TRUNCATE music_providers;

INSERT INTO music_providers VALUES('167afcf6-651f-42b6-8d70-1474101e7f44', 'Position Music', '', '', '', '', 'a55953bc-3e67-4843-bca7-01f9301155c6');


TRUNCATE music_provider_managers;

INSERT INTO music_provider_managers VALUES('d07c795c-8d03-4ef0-b07e-967a9b6ab2c4', '167afcf6-651f-42b6-8d70-1474101e7f44');


TRUNCATE scopes;

# user

INSERT INTO scopes VALUES('user.info', 'get user info', 'all,staff,record_label,admin');

INSERT INTO scopes VALUES('user.delete', 'delete user', 'admin');

# music

INSERT INTO scopes VALUES('music.list', 'list music', 'all,staff,record_label,admin');

INSERT INTO scopes VALUES('music.add', 'add music', 'staff,admin');

INSERT INTO scopes VALUES('music.delete', 'delete music', 'staff,admin');

INSERT INTO scopes VALUES('music.meta', 'music meta', 'staff,admin');

# album

INSERT INTO scopes VALUES('album.create', 'create album', 'staff,admin');

INSERT INTO scopes VALUES('album.update', 'update album', 'staff,admin');

INSERT INTO scopes VALUES('album.delete', 'delete album', 'staff,admin');

INSERT INTO scopes VALUES('album.read', 'read album', 'staff,admin');

# playlist

INSERT INTO scopes VALUES('playlist.create', 'create playlist', 'staff,admin');

INSERT INTO scopes VALUES('playlist.update', 'update playlist', 'staff,admin');

INSERT INTO scopes VALUES('playlist.delete', 'delete playlist', 'staff,admin');

INSERT INTO scopes VALUES('playlist.read', 'read playlist', 'staff,admin');
