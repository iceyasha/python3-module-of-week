import filecmp

dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report()
