def scan_resume(resume, resume_parser=None, resumeparse=None):
    from resume_parser import resumeparse
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}:>>{j}")


scan_resume("/Users/akshat/Desktop/Akshat Resume.pdf")