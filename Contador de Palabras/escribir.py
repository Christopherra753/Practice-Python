def write_txt(sentece, path):
  with open(path,"a") as file:
    file.write(f"{sentece}\n")