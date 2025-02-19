from langchain_teddynote.document_loaders.hwp import HWPLoader

# HWP Loader 객체 생성
loader = HWPLoader("./datasets/1편 학교법인/명예총장추대규정_19850301.hwp")

# 문서 로드
docs = loader.load()

for doc in docs:
    print(doc.page_content)