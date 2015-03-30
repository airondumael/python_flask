TRUNCATE users;

-- admin
INSERT INTO users(`user_id`, `email`, `role`) VALUES('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'airon@any.tv', 'admin');

-- staff
INSERT INTO users(`user_id`, `email`, `role`) VALUES('g4f9c597-1407-4a07-9ca9-3213f1acba65', 'lyndeniece@any.tv', 'music_provider');


TRUNCATE user_scopes;

-- admin scopes
INSERT INTO user_scopes VALUES  ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'self.info'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'user.info'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'user.delete'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'user.view_all'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.list'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.add'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.delete'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.meta'),
                                ('f4f9c597-1407-4a07-9ca9-3213f1acba65', 'music_provider.add');

-- music_provider scopes
INSERT INTO user_scopes VALUES  ('g4f9c597-1407-4a07-9ca9-3213f1acba65', 'self.info'),
                                ('g4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.list'),
                                ('g4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.add'),
                                ('g4f9c597-1407-4a07-9ca9-3213f1acba65', 'music.meta');


-- TRUNCATE scopes;


-- user

-- INSERT INTO scopes VALUES('user.info', 'get user info', 'all,staff,record_label,admin');

-- INSERT INTO scopes VALUES('user.delete', 'delete user', 'admin');

-- music

-- INSERT INTO scopes VALUES('music.list', 'list music', 'all,staff,record_label,admin');

-- INSERT INTO scopes VALUES('music.add', 'add music', 'staff,admin');

-- INSERT INTO scopes VALUES('music.delete', 'delete music', 'staff,admin');

-- INSERT INTO scopes VALUES('music.meta', 'music meta', 'staff,admin');

-- album

-- INSERT INTO scopes VALUES('album.create', 'create album', 'staff,admin');

-- INSERT INTO scopes VALUES('album.update', 'update album', 'staff,admin');

-- INSERT INTO scopes VALUES('album.delete', 'delete album', 'staff,admin');

-- INSERT INTO scopes VALUES('album.read', 'read album', 'staff,admin');

-- playlist

-- INSERT INTO scopes VALUES('playlist.create', 'create playlist', 'staff,admin');

-- INSERT INTO scopes VALUES('playlist.update', 'update playlist', 'staff,admin');

-- INSERT INTO scopes VALUES('playlist.delete', 'delete playlist', 'staff,admin');

-- INSERT INTO scopes VALUES('playlist.read', 'read playlist', 'staff,admin');
