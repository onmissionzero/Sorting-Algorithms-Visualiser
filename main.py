#SAV by Vignesh D

import pygame
import settings
import button
import drawinformation
import random
import algorithms
import sys

pygame.init()

#ButtonInstances
ButtonWidth = 122
ButtonHeight = 32
ButtonColor = (255,255,255)
sort_button = button.Button(10,10,ButtonWidth,ButtonHeight,ButtonColor,"Sort",(0,0,0))
algorithm_button = button.Button(10,60,ButtonWidth,ButtonHeight,ButtonColor,"Algorithms",(0,0,0))
generate_button = button.Button(10,110,ButtonWidth,ButtonHeight,ButtonColor,"Generate",(0,0,0))
back_button = button.Button(10,160,ButtonWidth,ButtonHeight,ButtonColor,"Back",(0,0,0))
ascending_button = button.Button(10,165,ButtonWidth,ButtonHeight,ButtonColor,"Ascending",(0,0,0))
descending_button = button.Button(10,215,ButtonWidth,ButtonHeight,ButtonColor,"Descending",(0,0,0))
pause_button = button.Button(10,280,ButtonWidth,ButtonHeight,ButtonColor,"Pause",(0,0,0))
customlist_button = button.Button(10,345,ButtonWidth,ButtonHeight,ButtonColor,"Custom List",(0,0,0))
exit_button = button.Button(10,410,ButtonWidth,ButtonHeight,ButtonColor,"Exit",(0,0,0))

WidthMul = 1.8
HeightMul = 1.4
bubblesort_button = button.Button(365,110,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Bubble Sort",(0,0,0))
insertionsort_button = button.Button(865,110,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Insertion Sort",(0,0,0))
selectionsort_button = button.Button(365,210,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Selection Sort",(0,0,0))
shellsort_button = button.Button(865,210,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Shell Sort",(0,0,0))
cocktailsort_button = button.Button(365,310,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Cocktail Sort",(0,0,0))

green_ascending_button = button.Button(10,165,ButtonWidth,ButtonHeight,(0,255,0),"Ascending",(0,0,0))
green_descending_button = button.Button(10,215,ButtonWidth,ButtonHeight,(0,255,0),"Descending",(0,0,0))

submit_button = button.Button(365,310,ButtonWidth*WidthMul,ButtonHeight*HeightMul,ButtonColor,"Submit",(0,0,0))

   
def main_menu_algorithm(sorting_algorithm):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        settings.WINDOW.fill((0,0,0))
        if back_button.draw():
            return sorting_algorithm
        if exit_button.draw():
            
            pygame.quit()
            exit()
        if insertionsort_button.draw():
            return algorithms.insertion_sort
        if bubblesort_button.draw():
            return algorithms.bubble_sort
        if selectionsort_button.draw():
            return algorithms.selection_sort
        if shellsort_button.draw():
            return algorithms.shell_sort
        if cocktailsort_button.draw():
            return algorithms.cocktail_sort

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(settings.WINDOW,(255,255,255),(140,0,4,settings.HEIGHT)) #Seperator
        pygame.display.update()
     
    pygame.quit()

def main_menu_customlist(lst):
    clock = pygame.time.Clock()
    run = True
    base_font = settings.font
    user_text = '' 
    input_rect = pygame.Rect(600, 200, 200, 50) 
    color_active = pygame.Color((255,255,255)) 
    color_passive = pygame.Color((200,200,200)) 
    color = color_passive 
    active = False

    while run:
        clock.tick(settings.FPS)
        settings.WINDOW.fill((0,0,0))
        if back_button.draw():
            return lst
        
        if exit_button.draw():
            pygame.quit()
            exit()

        if submit_button.draw():
            user_text_list = user_text.split(',')
            element_to_remove = ''
            while element_to_remove in user_text_list:
                user_text_list.remove(element_to_remove)
            int_list = [int(element) for element in user_text_list]           
            return int_list
        
        text_surface = settings.font.render('Enter your custom list:', False, (255, 255, 255))
        settings.WINDOW.blit(text_surface,(580,150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False

            if event.type == pygame.KEYDOWN: 

                # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 

                    # get text input from 0 to -1 i.e. end. 
                    user_text = user_text[:-1] 

                # Unicode standard is used for string 
                # formation 
                else:
                    if event.key in (pygame.K_COMMA, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                        user_text += event.unicode
        if active:
            color = color_active 
        else: 
            color = color_passive 
        pygame.draw.rect(settings.WINDOW, color, input_rect) 
        text = base_font.render(user_text, True, (0, 0, 0)) 
        # render at position stated in arguments 
        settings.WINDOW.blit(text, (input_rect.x+5, input_rect.y+5)) 
        # set width of textfield so that text cannot get 
        # outside of user's text input 
        input_rect.w = max(100, text.get_width()+10) 
        pygame.draw.rect(settings.WINDOW,(255,255,255),(140,0,4,settings.HEIGHT)) #Seperator
        pygame.display.update()


def generate_starting_list(n,min_val,max_val):
    lst = []
    
    for _ in range(n):
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst
          

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst
    inc = 0
    font = settings.lstfont
    offsetx = 160
    offsety = 45
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = (255, 255, 255)
        if i in color_positions:
            color = color_positions[i]
        inc += 1
        pygame.draw.rect(settings.WINDOW, color, (x + inc, y, draw_info.block_width, settings.HEIGHT))
        text = font.render(str(val), True, color)
        if(offsetx > settings.WIDTH-50):
            offsetx = 160
            offsety = offsety + 20
        offsetx = offsetx + 30
        text_rect = text.get_rect(topleft=(offsetx, offsety))
        settings.WINDOW.blit(text, text_rect)

    
def main():
    clock = pygame.time.Clock()
    n = 100
    min_val = 1
    max_val = 100
    lst = generate_starting_list(n,min_val,max_val)
    draw_info = drawinformation.DrawInformation(lst)
    run = True
    sorting = False
    ascending = True
    action = False
    sorting_algorithm = algorithms.bubble_sort
    sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

    while run:
        clock.tick(settings.FPS)
        settings.WINDOW.fill((0,0,0))
        font = settings.font
        SortAlgoName = getattr(sorting_algorithm, "__name__", str(sorting_algorithm))
        SortAlgoName = SortAlgoName.capitalize()
        SortAlgoName = SortAlgoName.replace('_',' ')
        SortAlgoNameRender = font.render(f'{SortAlgoName}', True,(255,255,255))
        settings.WINDOW.blit(SortAlgoNameRender, (160,15))
        if sorting:
            action = True
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                action = False
        else:
            draw_list(draw_info)   

        if sort_button.draw(sorting) and not action:
            sorting = True

        if pause_button.draw() and action:
            action = False
            sorting = False

        if ascending:
            if green_ascending_button.draw() and not action:
                ascending = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
        if descending_button.draw(sorting) and not action:
                ascending = False
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if not ascending:
            if ascending_button.draw(sorting) and not action:
                ascending = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
            if green_descending_button.draw() and not action:
                ascending = False
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if algorithm_button.draw(sorting) and not action:
            sorting_algorithm = main_menu_algorithm(sorting_algorithm)
            sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if generate_button.draw(sorting) and not action:
            lst = generate_starting_list(n,min_val,max_val)
            draw_info.set_list(lst)
            sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
        
        if customlist_button.draw(sorting) and not action:
            lst = main_menu_customlist(lst)
            draw_info.set_list(lst)
            sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
        
        if exit_button.draw(sorting) and not action:
            pygame.quit()
            exit()

        pygame.draw.rect(settings.WINDOW,(255,255,255),(140,0,4,settings.HEIGHT)) #Seperator
        pygame.draw.rect(settings.WINDOW,(255,255,255),(6, 155, 130, 108),2) #Asc, Desc Box
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #and not action: # !close when pressing 'x' on titlebar
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
