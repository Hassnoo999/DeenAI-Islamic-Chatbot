from nicegui import ui

# === Theme Toggle (Optional) ===

with ui.row().classes('absolute top-4 right-4 z-10'):
    ui.dark_mode().bind_value(ui.toggle(['🌞', '🌙']))

# === ROUTE 1: LANDING PAGE ===
@ui.page('/')
def landing():
    with ui.element('div').classes('fixed inset-0 -z-10 overflow-hidden'):
        ui.video('D:\Air Uni Notes\Semester 4\Information Retrieval\IR Project\GitHub IR Project\Python Code Files\Front-end\kabba.mp4',
                  autoplay=True, muted=True, loop=True).classes(
            'w-full h-full object-cover'
        ).style('filter: blur(3px); transform: scale(1.05);')

    with ui.column().classes('absolute top-0 left-0 w-full h-full flex flex-col items-center justify-center text-center'):
        ui.label('Welcome to Deen AI').classes(
            'text-4xl md:text-6xl font-bold mb-4 text-[#f5d596]'
        ).style('text-shadow: 1px 1px 5px rgba(0,0,0,0.7);')

        ui.label('Ask anything about Islam, powered by authentic sources.').classes(
            'text-base md:text-xl mb-8 text-[#f8f8f8]'
        ).style('text-shadow: 1px 1px 4px rgba(0,0,0,0.6);')

        ui.link('Enter Chat', '/chat').classes(
            'bg-[#f5d596] bg-opacity-80 hover:bg-opacity-100 font-bold text-[#020a37] px-6 py-3 rounded-full shadow-lg text-lg transition-all duration-300'
        ).style('box-shadow: 0 8px 24px rgba(0,0,0,0.3);')


# === ROUTE 2: CHAT PAGE ===
@ui.page('/chat')
def chat_ui():
    chat_history = []

    def send_message():
        user_msg = input_box.value.strip()
        if not user_msg:
            return

        chat_history.append(('user', user_msg))
        with chat_area:
            render_message('user', user_msg)

        # Replace with your actual response logic
        bot_reply = "This is where your model response goes."
        chat_history.append(('bot', bot_reply))
        with chat_area:
            render_message('bot', bot_reply)

        input_box.value = ''

    def render_message(sender, text):
        align = 'justify-end' if sender == 'user' else 'justify-start'
        bubble_color = 'bg-[#0e5449] text-white' if sender == 'user' else 'bg-[#f5d596] text-[#1a3a5f]'
        
        with ui.row().classes(f'w-full {align} mb-2'):
            ui.label(text).classes(
                f'{bubble_color} px-4 py-3 rounded-lg max-w-[80%] shadow-sm'
            ).style('word-wrap: break-word;')

    # === Page Layout ===
    with ui.column().classes('h-screen w-screen bg-gradient-to-b from-[#f8f8f8] to-[#e6d8c4] overflow-hidden'):

        # === Fixed Header ===
        with ui.row().classes('fixed top-0 left-0 w-full justify-center items-center shadow-md z-10 h-20').style('background-color: #0e5449;'):
            with ui.row().classes('items-center gap-2 max-w-6xl w-full px-4'):
                ui.image('D:\Air Uni Notes\Semester 4\Information Retrieval\IR Project\GitHub IR Project\Python Code Files\Front-end\Logo.png').classes('w-12 h-12')
                ui.label('DeenAI').classes('text-2xl font-semibold').style('color:#f5d596;')

        # === Scrollable Chat Area ===
        with ui.scroll_area().classes(
            'flex-1 w-full pt-20 pb-24 px-4 md:px-8 overflow-y-auto overflow-x-hidden max-w-screen'
        ) as chat_area:
            render_message('bot', 'Assalamu Alaikum! Ask me anything about Islam.')

        # === Fixed Input Bar at Bottom ===
        with ui.row().classes('fixed bottom-0 left-0 w-full px-4 py-3 z-10 justify-center items-center').style('background-color: #0e5449;'):

            def on_keydown(e):
                if e.args.get('key') == 'Enter':
                    send_message()
                    e.prevent_default()

            with ui.row().classes('w-full max-w-4xl items-center gap-2'):
                input_box = ui.input('Ask something about Islam...').props('dense').classes(
                    'flex-grow px-4 py-3 border-2 border-[#f5d596] rounded-full bg-white'
                ).on('keydown', on_keydown)

                # Send button (image)
                ui.image('D:\Air Uni Notes\Semester 4\Information Retrieval\IR Project\GitHub IR Project\Python Code Files\Front-end\send-button-green.png').on('click', send_message).classes(
                    'cursor-pointer w-10 h-10 hover:scale-110 transition-transform'
                )
                
    # === Page Layout ===
    with ui.column().classes('h-screen w-screen bg-gray overflow-hidden'):

        # === Fixed Header ===
        with ui.row().classes('fixed top-0 left-0 w-full justify-center items-center shadow-md z-10').style('background-color: #0e5449;'):
            with ui.row().classes('items-center gap-2'):
                ui.image('D:\Air Uni Notes\Semester 4\Information Retrieval\IR Project\GitHub IR Project\Python Code Files\Front-end\Logo.png').classes('w-20 h-20')
                ui.label('DeenAI').classes('text-2xl font-semibold').style('color:#f5d596;')

        # === Scrollable Chat Area ===
        # In your chat_area container, add these classes:
        with ui.scroll_area().classes('flex-1 w-full pt-20 pb-28 px-6 overflow-y-auto overflow-x-auto max-w-screen'
        ) as chat_area:
            render_message('bot', 'Assalamu Alaikum! Ask me anything about Islam.')

        # === Fixed Input Bar at Bottom ===
        with ui.row().classes('fixed bottom-0 left-0 w-full bg-gray px-6 py-3 z-10 justify-center items-center shadow-inner'):

            def on_keydown(e):
                if e.args.get('key') == 'Enter':
                    send_message()
                    e.prevent_default()

            with ui.row().classes('w-full max-w-4xl items-center gap-2'):
                input_box = ui.input('Ask something about Islam...').props('dense').classes(
                    'flex-grow px-4 py-2 border border-gray-300 rounded-full'
                ).on('keydown', on_keydown)

                # Send button (image)
                ui.image('D:\Air Uni Notes\Semester 4\Information Retrieval\IR Project\GitHub IR Project\Python Code Files\Front-end\send-button-green.png').on('click', send_message).classes(
                    'cursor-pointer w-10 h-10'
                )

# === RUN APP ===
ui.run(title='DeenAI Chatbot')
