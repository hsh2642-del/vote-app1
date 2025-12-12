import gradio as gr

def vote_app():
    candidates = {}
    invalid_votes = 0

    # 후보 등록
    num = gr.Number(label="등록할 후보 수", value=2)
    cand_inputs = []

    def set_candidates(n):
        nonlocal cand_inputs
        cand_inputs = [gr.Textbox(label=f"{i+1}번 후보 이름") for i in range(int(n))]
        return cand_inputs

    # 투표 기능
    voters = gr.Number(label="투표 인원 수", value=3)

    def run_vote(*votes):
        nonlocal invalid_votes
        counts = {name: 0 for name in votes[:-1] if name != ""}  # 후보 dict 생성
        vote_list = votes[-1]  # 유권자들의 투표 기록

        for v in vote_list.split("\n"):
            v = v.strip()
            if v in counts:
                counts[v] += 1
            else:
                invalid_votes += 1

        # 당선자 계산
        max_votes = max(counts.values()) if counts else 0
        winners = [name for name, count in counts.items() if count == max_votes]

        # 출력 문자열
        result = "📊 **최종 투표 결과**\n\n"
        for k, v in counts.items():
            result += f"- **{k}: {v}표**\n"

        result += f"\n❌ **무효표: {invalid_votes}표**\n"

        if len(winners) == 1:
            result += f"\n🏆 **당선자: {winners[0]} ({max_votes}표)**"
        else:
            result += "\n🏆 **동점자:** " + ", ".join(winners)

        return result

    with gr.Blocks() as demo:
        gr.Markdown("# 🗳️ 온라인 투표 프로그램")
        gr.Markdown("후보를 등록하고 유권자 투표 결과를 자동으로 계산해줍니다.")

        num_input = gr.Number(label="등록할 후보 수", value=2)
        btn_set = gr.Button("후보 입력창 만들기")
        cand_area = gr.Column()
        btn_set.click(set_candidates, inputs=num_input, outputs=cand_area)

        gr.Markdown("### ✏️ 유권자들의 투표 입력 (줄바꿈으로 구분)")
        vote_text = gr.Textbox(lines=10, label="예: 홍길동\n김철수\n홍길동")

        run_bt_
