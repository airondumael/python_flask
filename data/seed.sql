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
