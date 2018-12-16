from beepo import morse

code_table = morse.load_codetable()
morse.play_init()
sounds = morse.load_sounds()
morse.play_code(code_table, sounds, 'a')
