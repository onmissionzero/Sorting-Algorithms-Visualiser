#SAV by Vignesh D

import pygame
import settings
import button
import drawinformation
import random
import algorithms

pygame.init()



#LoadImages
MainMenu_SortButton = pygame.image.load("Assets\\button_sort.png").convert_alpha()
MainMenu_GenerateButton = pygame.image.load("Assets\\button_generate.png").convert_alpha()
MainMenu_AlgorithmButton = pygame.image.load("Assets\\button_algorithm.png").convert_alpha()
MainMenu_BackButton = pygame.image.load("Assets\\button_back.png").convert_alpha()
MainMenu_ExitButton = pygame.image.load("Assets\\button_exit.png").convert_alpha()
MainMenu_PauseButton = pygame.image.load("Assets\\button_pause.png").convert_alpha()
MainMenu_AscendingButton = pygame.image.load("Assets\\button_ascending.png").convert_alpha()
MainMenu_DescendingButton = pygame.image.load("Assets\\button_descending.png").convert_alpha()
BubbleSortButton = pygame.image.load("Assets\\button_bubblesort.png").convert_alpha()
InsertionSortButton = pygame.image.load("Assets\\button_insertionsort.png").convert_alpha()
SelectionSortButton = pygame.image.load("Assets\\button_selectionsort.png").convert_alpha()
ShellSortButton = pygame.image.load("Assets\\button_shellsort.png").convert_alpha()
CocktailSortButton = pygame.image.load("Assets\\button_cocktailsort.png").convert_alpha()

MainMenu_GreenAscendingButton = pygame.image.load("Assets\\button_greenascending.png").convert_alpha()
MainMenu_GreenDescendingButton = pygame.image.load("Assets\\button_greendescending.png").convert_alpha()

MainMenu_ImageScale = 0.6
AlgoMenu_ImageScale = 1.0


#ButtonInstances
sort_button = button.Button(MainMenu_SortButton,10,10,MainMenu_ImageScale)
algorithm_button = button.Button(MainMenu_AlgorithmButton,10,60,MainMenu_ImageScale)
generate_button = button.Button(MainMenu_GenerateButton,10,110,MainMenu_ImageScale)
back_button = button.Button(MainMenu_BackButton,10,160,MainMenu_ImageScale)
ascending_button = button.Button(MainMenu_AscendingButton,10,165,MainMenu_ImageScale)
descending_button = button.Button(MainMenu_DescendingButton,10,215,MainMenu_ImageScale)
pause_button = button.Button(MainMenu_PauseButton,10,280,MainMenu_ImageScale)
exit_button = button.Button(MainMenu_ExitButton,10,345,MainMenu_ImageScale)


bubblesort_button = button.Button(BubbleSortButton,365,110,AlgoMenu_ImageScale)
insertionsort_button = button.Button(InsertionSortButton,865,110,AlgoMenu_ImageScale)
selectionsort_button = button.Button(SelectionSortButton,365,210,AlgoMenu_ImageScale)
shellsort_button = button.Button(ShellSortButton,865,210,AlgoMenu_ImageScale)
cocktailsort_button = button.Button(CocktailSortButton,500,400,AlgoMenu_ImageScale)

green_ascending_button = button.Button(MainMenu_GreenAscendingButton,10,165,MainMenu_ImageScale)
green_descending_button = button.Button(MainMenu_GreenDescendingButton,10,215,MainMenu_ImageScale)


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


def generate_starting_list(n,min_val,max_val):
    lst = []
    
    for _ in range(n):
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst



def draw_list(draw_info,color_positions={},clear_bg=False):
    lst = draw_info.lst

    inc = 0
    for i,val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        
        color = (255,255,255)
        if i in color_positions:
            color = color_positions[i]
        inc+=1
        pygame.draw.rect(settings.WINDOW,color,(x+inc,y,draw_info.block_width,settings.HEIGHT))
 



def main():
    clock = pygame.time.Clock()
    n = 100
    min_val = 0
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
        #print(clock.get_fps())
        settings.WINDOW.fill((0,0,0))
        font = settings.font
        SortAlgoName = getattr(sorting_algorithm, "__name__", str(sorting_algorithm))
        SortAlgoName = SortAlgoName.capitalize()
        SortAlgoName = SortAlgoName.replace('_',' ')
        text = font.render(f'{SortAlgoName}', True,(255,255,255))
        settings.WINDOW.blit(text, (10,445))

        if sorting:
            action = True
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                action = False
        else:
            draw_list(draw_info)   

        if sort_button.draw() and not action:
            sorting = True

        if pause_button.draw() and action:
            action = False
            sorting = False

        if ascending:
            if green_ascending_button.draw() and not action:
                ascending = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
        if descending_button.draw() and not action:
                ascending = False
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if not ascending:
            if ascending_button.draw() and not action:
                ascending = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
            if green_descending_button.draw() and not action:
                ascending = False
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if algorithm_button.draw() and not action:
            sorting_algorithm = main_menu_algorithm(sorting_algorithm)
            sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

        if generate_button.draw() and not action:
            lst = generate_starting_list(n,min_val,max_val)
            draw_info.set_list(lst)
            sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)
        
        if exit_button.draw() and not action:
            
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
