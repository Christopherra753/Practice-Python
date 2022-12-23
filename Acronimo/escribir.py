def write_txt(sentece,acronimo,path):
  with open(path,"a") as file:
    file.write(f"{sentece} - {acronimo}\n")