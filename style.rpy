# This file is responsible for creating and defining the default styles
# used by the system.

# This file should be considered part of the Ren'Py library, and not
# something that needs to be modified by the user. Instead, just update
# the appropriate style property in an init: block in your script.
#
# For example, to change the default window backgrounds to a
# transparent dark red, add:
#
# init:
#     $ style.window.background = renpy.Solid((128, 0, 0, 128)
#
# to your script. No need to mess around here, it will just make your
# life harder when a new version of Ren'Py is released.

init -100:
    python hide:

        style.create('default', None,
                     'The default style that all styles inherit from.')

        # Text properties.
        style.default.font = "Vera.ttf"
        style.default.size = 22
        style.default.color = (255, 255, 255, 255)
        style.default.drop_shadow = (2, 2)
        style.default.drop_shadow_color = (0, 0, 0, 128)

        # Window properties.
        style.default.background = None
        style.default.xpadding = 0
        style.default.ypadding = 0
        style.default.xmargin = 0
        style.default.ymargin = 0
        style.default.xfill = False
        style.default.yfill = False
        style.default.xminimum = 0 # Includes margins and padding.
        style.default.yminimum = 0 # Includes margins and padding.

        # Placement properties.
        style.default.xpos = 0
        style.default.ypos = 0
        style.default.xanchor = 'left'
        style.default.yanchor = 'top'

        # This style controls the default placement of images on the screen.

        style.create('image_placement', None,
                     'This style is used to control the default placement of images on the screen.')

        style.image_placement.xpos = 0.5
        style.image_placement.ypos = 1.0
        style.image_placement.xanchor = 'center'
        style.image_placement.yanchor = 'bottom'

        # Styles that are used for dialogue.

        style.create('say_label', 'default',
                     'The style that the label text of a two-argument say statement is in.')

        style.create('say_dialogue', 'default',
                     'The style that the dialogue text of a two-argument say statement is in.')

        style.create('say_thought', 'default',
                     'The style that that the text of a one-argument say statement is in.')

        # Styles that are used for menus.

        style.create('menu_caption', 'default',
                     'The style that menu captions are styled in.')

        style.create('menu_choice_selected', 'default',
                     'The style that selected menu choices are rendered in.')

        style.menu_choice_selected.color = (255, 255, 0, 255) # yellow

        style.create('menu_choice_unselected', 'default',
                     'The style that unselected menu choices are rendered in.')

        style.menu_choice_unselected.color = (0, 255, 255, 255) # cyan


        # Styles that are used for windows that contain dialogue or
        # menus.

        style.create('window', 'default',
                     'The base style for large windows that have content in them.')

        style.window.background = renpy.Solid((0, 0, 128, 128))
        style.window.xpadding = 10
        style.window.ypadding = 5
        style.window.xmargin = 10
        style.window.ymargin = 5
        style.window.xfill = True
        style.window.yfill = False
        style.window.xminimum = 0 # Includes margins and padding.
        style.window.yminimum = 150 # Includes margins and padding.

        style.window.xpos = 0.5
        style.window.ypos = 1.0
        style.window.xanchor = 'center'
        style.window.yanchor = 'bottom'

        style.create('window_say', 'window',
                     'The default style for windows containing dialogue.')

        style.create('window_menu', 'window',
                     'The default style for windows containing a menu.') 


        # Styles that are used by all Buttons.
        style.create('button', 'default',
                     'The base style for all buttons.')

        style.create('button_idle', 'button',
                     'The style that is used by default by buttons when the mouse is not hovering over the button.')

        style.create('button_hover', 'button',
                     'The style that is used by default by buttons when the mouse is above the button.')

        # Styles that are used for the label of TextButtons.
        style.create('button_text', 'default',
                     'The base style used for text that is a label of a button.')


        style.create('button_idle_text', 'button_text',
                     'The style that is used for text that is displayed as the label of a button that is idle.')

        style.create('button_hover_text', 'button_text',
                     'The style that is used for text that is displayed as the label of a button that is hovered.')
        
        style.button_text.xpos = 0.5
        style.button_text.xanchor = 'center'
        style.button_text.size = 32
        style.button_idle_text.color = (0, 255, 255, 255)
        style.button_hover_text.color = (255, 255, 0, 255)
        

        # Styles that are used when laying out the main menu.
        style.create('mm_root', 'default',
                     'The root window of the main menu.')

        style.mm_root.background = renpy.Image("mainmenu.jpg")

        style.create('mm_menu_window', 'default',
                     'A window containing the actual menu choices in the main menu.')

        style.mm_menu_window.xpos = 0.5
        style.mm_menu_window.xanchor = 'center'
        style.mm_menu_window.ypos = 0.6
        style.mm_menu_window.yanchor = 'top'

        
