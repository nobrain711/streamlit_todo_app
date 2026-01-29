# import library
## Streamlit import alias st
import streamlit as st

# class
class Todo:
    """
    할 일과 여부를 객채로 관리하기 위해서 작성한 클래스
    """
    def __init__(self, task: str, done: bool=False) -> None:
        """
        객체를 생성할 때 초기에 필요로한 값

        :param task: str = 할 일 or 스케줄
        :param done: bool = 상태 default=False
        """
        self.__task: str = task
        self.__done: bool = done

    # def __str__(self) -> str:
    #     """
    #     입력하신 Task에 대한 상태를 출력합니다.
    #     :return: str
    #     """
    #     return f'task: {self.__task}\t\tdone: {self.__done}'

    def __repr__(self) -> str:
        # 객체가 리스트 안에 있을 때 리스트 인의 요소들을 출력할 때 이용합니다.
        # repr은 eval()로 다시 객체로 바꿀 수 있는 문자열을 형태로 작성하는게 원칙
        """
        조회를 요청한 Task의 상태를 출력합니다.
        :return:
        """
        return f'Todo(task="{self.__task}", done={self.__done})'

    def get_task(self) -> str:
        """
        이 함수를 호춣하면 __task의 값을 반환합니다.

        :return: str
        """
        return self.__task

    def get_done(self) -> bool:
        """
        이 매소드를 호출하면 __done의 값을 반환합니다.

        :return: bool
        """
        return self.__done

    def set_done(self, done: bool) -> None:
        """
        이 매서드를 호출하면서 매게변수를 주면 done의 값을 변경합니다.

        :param done: bool
        :return: None
        """
        self.__done = done

# functional
## todo객체를 생성해서 todos list에 넣어주는 함수
def add_todo() -> None:
    """
    todo객체를 생성해서 todos list에 넣어주는 함수
    """
    # log
    print('add todo running')
    print(f'streamlit session state new_task: {st.session_state.new_task}')
    task = Todo(st.session_state.new_task)
    print(f'succeed added new_task: {task}')
    st.session_state.todos.append(task)
    print(f'succeed streamlit session added new_task: {st.session_state.todos}')
    # streamlit session state에 new_task의 값 초기화
    st.session_state.new_task = ''
    print(f'streamlit session state new_task clear: {st.session_state.new_task}')

    return None

## todo의 done의 값을 변경하는 함수
def toggle_done(i: int) -> None:
    """
    todo의 done의 값을 변경하는 함수

    index: int todos에서 변경하려는 요소의 index

    :return: None
    """
    print('toggle done running')
    print(f'task {i} done value exchange before: {st.session_state.todos[i]}')
    task=st.session_state.todos[i]
    task.set_done(not task.get_done())
    print(f'task {i} done value exchange after: {st.session_state.todos[i]}')

    return None

# __repr__ 설명
# todo = Todo("숙제하기")
# print(id(todo))
# todo2 = eval(repr(todo))
# print(todo2)

# variable
## todos(todo 객체를 답을 리스트)
if 'todos' not in st.session_state:
    st.session_state.todos = []

# front
## title
st.title('📝 Todo list 📝')

## divider
## - title과 공간을 구분하기 위해서 구분선 추가
st.divider()

## textbox
st.text_input(
    label='새로운 할 일 추가',     # text_box위로 출력
    key='new_task',             # streamlit session state key로 추가되는 이름
    on_change=add_todo          # text_box에 내용이 추가되면 자동으로 함수 호출
)

## show todo list
if st.session_state.todos:
    # todos에 요소가 있으면 출력하기
    for index, todo in enumerate(st.session_state.todos):
        # enumerate를 이용해서 todos의 index도 같이 출력
        # st.write(f'{index}번째 todo => {todo}')
        col1, col2 = st.columns([0.1, 0.9]) # streamlit으로 2개의 열을 가지는 행을 생성
        col1.checkbox(label=f'{index + 1}',     # checkbox옆으로 index출력
                      value=todo.get_task(),    # 값은 Todo의 task 값을 지정
                      key=f'done_{index}',      # streamlit session state에 key를 done_todos의 index로 생성
                      on_change=toggle_done,    # 내용이 변경되면 toggle_done을 호출
                      args={index})             # 매게변수는 index로 넘겨 줌
        col2.markdown(f'~~{todo.get_task()}~~'if todo.get_done() else todo.get_task())  # ~~는 밑줄을 의미함
                                                                                        # 삼항 연산자로 todo의 done을 값으로 밑줄 표시여부 선택
else:
    # todos에 요소가 없으면 info를 출력
    st.info('할 일을 추가해 주세요❗❗❗')