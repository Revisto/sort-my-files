from os import rename, path, makedirs, listdir

class File:
    def move_series(self, filename, series_name, season, quality):
        series_path = f"{series_name}/S{season}/{quality}p"
        try:
            makedirs(series_path)
        except:
            pass
        rename(filename, f"{series_path}/{filename}")
        return True

    def ls(self):
        onlyfiles = [f for f in listdir() if path.isfile(path.join(f))]
        return onlyfiles