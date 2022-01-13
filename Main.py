import pygame
import sys
import threading
import random
pygame.init()

def func():
    pass

def check_time():
    global line_time_16, line_time_2, level, old_score
    if score % 1000 == 0 and score != 0 and old_score != score:
        line_time_16 *= 0.95
        line_time_2 *= 0.9
        level += 1
        old_score = score

FPS = 60
list_of_nums = []
black = (0, 0, 0)
white = (255, 255, 255)
height = 600 # screen size
width = 600
score = old_score = new_score = 0
level = 0
box_height = 60
zero_height = 459
line_time_2 = 5 # line time (seconds)
line_time_16 = 20
num_line = 0 # amount of lines
play = False
system = 2
list_of_lines = []
list_of_small_rects = []
list_of_primes = []
list_of_examples = []
list_of_status = []
col = 0
font = pygame.font.Font(None, 60)
font1 = pygame.font.Font(None, 50)
header_font = pygame.font.Font(None, 40) # font
nums_font = pygame.font.Font(None, 50)
nums2_font = pygame.font.Font(None, 40)
nums16_font = pygame.font.Font(None, 30)
x_font = pygame.font.SysFont("segoeuisymbol", 30)
x2_font = pygame.font.SysFont("segoeuisymbol", 30)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bingame')
screen.fill(black)
clock = pygame.time.Clock()

pygame.display.update()

class Background(pygame.sprite.Sprite): # Background
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def check_equal(lst, num, syst):
    string = ''.join([str(i) for i in lst])
    if syst == 2:
        x = int(string, 2)
        return x == num
    elif syst == 16:
        x = int(string, 16)
        return x == num


def count_sum(lst, syst):
    string = ''.join([str(i) for i in lst])
    if syst == 2:
        x = int(string, 2)
        return x
    elif syst == 16:
        x = int(string, 16)
        return x



def update_screen(): # standart screen
    file = open('record.txt', 'r')
    txt = file.read()
    file.close()
    rec1 = int(txt.split('\n')[0])
    rec2 = int(txt.split('\n')[1])
    screen.fill(white)
    screen.blit(BackGround.image, BackGround.rect)
    screen.blit(footer, (0, 520)) # down
    screen.blit(header, (0, 0)) # up
    pygame.draw.line(screen, white,
                 [0, 40],
                 [600, 40], 3)
    pygame.draw.line(screen, white,
                 [0, 100],
                 [600, 100], 3)
    pygame.draw.line(screen, white,
                 [0, 520],
                 [600, 520], 3)
    dop_text = x2_font.render('★', True, white)  # score
    text_score = header_font.render(f'Счёт: {score}', True, white) # score
    screen.blit(text_score, (width // 2 - 47, 10))
    if system == 2:
        if score >= rec1:
            screen.blit(dop_text, (width // 2 - 47 + text_score.get_width() + 10, 0))
    elif system == 16:
        if score >= rec2:
            screen.blit(dop_text, (width // 2 - 47 + text_score.get_width() + 10, 0))
    text_level = header_font.render(f'Уровень: {level}', True, white) # level
    screen.blit(text_level, (10, 10))
    zero_height = 459
    for i in range(len(list_of_examples)):
        # pygame.draw.rect(screen, 'white', (60, zero_height, 480, box_height))
        zero_width = 130
        if system == 16:
            text_num = nums16_font.render(str(list_of_examples[i]), True, white)
            text_num_res = nums16_font.render(str(count_sum(list_of_primes[i], system)), True, white)
        else:
            text_num = nums2_font.render(str(list_of_examples[i]), True, white)
            text_num_res = nums2_font.render(str(count_sum(list_of_primes[i], system)), True, white)
        screen.blit(text_num, (10, zero_height + 20))
        screen.blit(text_num_res, (490, zero_height + 20))
        for j in range(6):
            text_nums = nums_font.render(str(list_of_primes[i][j]), True, white)
            pygame.draw.rect(screen, (50, 50, 50), (zero_width, zero_height + 5, 50, box_height - 10))
            screen.blit(text_nums, (zero_width + 25 - text_nums.get_width() // 2, zero_height + 30 - text_nums.get_height() // 2))
            zero_width += 60
        zero_height -= box_height

def base_draw():
    screen.fill(white)
    screen.blit(BackGround.image, BackGround.rect)


def draw_new_line(): # function for drawing bew lines
    global num_line, tread, col, zero_height
    num_line += 1
    list_of_status.append(False)
    list_of_examples.append(random.randint(1, system ** 6 - 1))
    list_of_primes.append(['0', '0', '0', '0', '0', '0'])
    list_of_lines.append(col)
    zero_width = 130
    list_of_small_rects.append([])
    for i in range(6):
        list_of_small_rects[-1].append((zero_width, zero_height + 5, 50, box_height - 10))
        zero_width += 60
    zero_height -= box_height

    col += 1
    if system == 16:
        tread = threading.Timer(line_time_16, draw_new_line)
    else:
        tread = threading.Timer(line_time_2, draw_new_line)

    tread.start()

def first_screen(): # screen with settings to play
    global play, system, list_of_nums
    system = 2
    rec = False
    base_draw()
    rect_alpha = 0
    rect2_alpha = 0
    rect16_alpha = 0
    rect_records_alpha = 0
    rect = pygame.Rect((200, 275, 200, 50))
    rect_2 = pygame.Rect((200, 155, 90, 100))
    rect_16 = pygame.Rect((310, 155, 90, 100))
    rect_records = pygame.Rect((10, 10, 30, 30))
    text_play = font1.render('Играть', True, white)  # level
    text_2 = font.render('2', True, white)  # level
    text_16 = font.render('16', True, white)  # level
    text_records = x_font.render('⌕', True, white)
    def local():
        rect_surf = pygame.Surface((200, 50))
        rect2_surf = pygame.Surface((90, 100))
        rect16_surf = pygame.Surface((90, 100))
        rect_records_surf = pygame.Surface((30, 30))
        rect_surf.fill(black)
        rect2_surf.fill(black)
        rect16_surf.fill(black)
        rect_records_surf.fill(black)
        rect_surf.set_alpha(rect_alpha)
        rect2_surf.set_alpha(rect2_alpha)
        rect16_surf.set_alpha(rect16_alpha)
        rect_records_surf.set_alpha(rect_records_alpha)
        screen.blit(rect_surf, (200, 275))
        screen.blit(rect2_surf, (200, 155))
        screen.blit(rect16_surf, (310, 155))
        screen.blit(rect_records_surf, (10, 10))
        screen.blit(text_play, (300 - text_play.get_width() // 2, 300 - text_play.get_height() // 2))
        screen.blit(text_2, (245 - text_2.get_width() // 2, 205 - text_2.get_height() // 2))
        screen.blit(text_16, (355 - text_16.get_width() // 2, 205 - text_16.get_height() // 2))
        screen.blit(text_records, (25 - text_records.get_width() // 2, 25 - text_records.get_height() // 2))
        pygame.draw.rect(screen, white, (200, 275, 200, 50), 1)
        pygame.draw.rect(screen, white, (10, 10, 30, 30), 1)
        if system == 2:
            pygame.draw.rect(screen, white, (200, 155, 90, 100), 1)
        elif system == 16:
            pygame.draw.rect(screen, white, (310, 155, 90, 100), 1)

    local()
    pygame.display.update()
    while not play:
        for i in pygame.event.get():
            if i.type == pygame.MOUSEMOTION:
                if rect.collidepoint(i.pos):
                    rect_alpha = 100
                    rect2_alpha = 0
                    rect16_alpha = 0
                    rect_records_alpha = 0
                elif rect_2.collidepoint(i.pos):
                    rect_alpha = 0
                    if system != 2:
                        rect2_alpha = 100
                    rect16_alpha = 0
                    rect_records_alpha = 0
                elif rect_16.collidepoint(i.pos):
                    rect_alpha = 0
                    rect2_alpha = 0
                    if system != 16:
                        rect16_alpha = 100
                    rect_records_alpha = 0
                elif rect_records.collidepoint(i.pos):
                    rect_alpha = 0
                    rect2_alpha = 0
                    rect16_alpha = 0
                    rect_records_alpha = 100
                else:
                    rect_alpha = 0
                    rect2_alpha = 0
                    rect16_alpha = 0
                    rect_records_alpha = 0

            if i.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(i.pos):
                play = True
            if i.type == pygame.MOUSEBUTTONDOWN and rect_2.collidepoint(i.pos):
                system = 2
            if i.type == pygame.MOUSEBUTTONDOWN and rect_16.collidepoint(i.pos):
                system = 16
            if i.type == pygame.MOUSEBUTTONDOWN and rect_records.collidepoint(i.pos):
                rec = True
                break
            if i.type == pygame.QUIT:
                sys.exit()
        if system == 16:
            list_of_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        elif system == 2:
            list_of_nums = ['0', '1']
        if rec:
            records_screen()
        base_draw()
        local()
        pygame.draw.rect(screen, white, (200, 275, 200, 50), 1)
        pygame.display.update()



def records_screen():
    rect_alpha = 0
    rect = pygame.Rect((10, 10, 30, 30))
    text = x_font.render('←', True, white)
    file = open('record.txt', 'r')
    txt = file.read()
    file.close()
    rec1 = txt.split('\n')[0]
    rec2 = txt.split('\n')[1]
    def local():
        screen.fill(white)
        screen.blit(BackGround.image, BackGround.rect)
        txt1 = font.render('Your record', True, white)
        screen.blit(txt1, (300 - txt1.get_width() // 2, 50))
        txt2 = font.render(f'2x: {rec1}', True, white)
        screen.blit(txt2, (300 - txt2.get_width() // 2, 200))
        txt3 = font.render(f'16x: {rec2}', True, white)
        screen.blit(txt3, (300 - txt3.get_width() // 2, 250))
        rect_surf = pygame.Surface((30, 30))
        rect_surf.fill(black)
        rect_surf.set_alpha(rect_alpha)
        screen.blit(rect_surf, (10, 10))
        screen.blit(text, (25 - text.get_width() // 2, 21 - text.get_height() // 2))
        pygame.draw.rect(screen, white, (10, 10, 30, 30), 1)

    play = False
    while not play:
        local()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.MOUSEMOTION:
                if rect.collidepoint(i.pos):
                    rect_alpha = 100
                else:
                    rect_alpha = 0
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(i.pos):
                    play = True


        pygame.display.update()
    first_screen()


def last_screen():
    global list_of_nums, score, old_score, new_score, level, box_height, zero_height, line_time_2, line_time_16, num_line, list_of_lines, list_of_small_rects, list_of_primes, list_of_examples, list_of_status, col
    file = open('record.txt', 'r')
    txt = file.read()
    file.close()
    rec1 = int(txt.split('\n')[0])
    rec2 = int(txt.split('\n')[1])
    back_alpha = 0
    exit_alpha = 0
    back_rect = pygame.Rect((175, 300, 250, 50))
    exit_rect = pygame.Rect((175, 400, 250, 50))
    text_back = font1.render('To menu', True, white)  # level
    text_exit = font.render('Exit', True, white)  # level
    def local():
        back_surf = pygame.Surface((250, 50))
        exit_surf = pygame.Surface((250, 50))
        back_surf.fill(black)
        exit_surf.fill(black)
        back_surf.set_alpha(back_alpha)
        exit_surf.set_alpha(exit_alpha)
        screen.fill(white)
        screen.blit(BackGround.image, BackGround.rect)
        txt1 = font1.render('GAME OVER', True, white)
        screen.blit(txt1, (300 - txt1.get_width() // 2, 20))
        txt2 = font.render(f'Your score: {score}', True, white)
        txt3 = font.render('It is your new record!', True, white)
        if system == 2:
            if rec1 <= score:
                file = open('record.txt', 'w')
                file.write(str(score) + '\n' + str(rec2))
                file.close()
                screen.blit(txt3, (300 - txt3.get_width() // 2, 150))
        elif system == 16:
            if rec2 <= score:
                file = open('record.txt', 'w')
                file.write(str(rec1) + '\n' + str(score))
                file.close()
                screen.blit(txt3, (300 - txt3.get_width() // 2, 150))
        screen.blit(txt2, (300 - txt2.get_width() // 2, 100))
        screen.blit(back_surf, (175, 300))
        screen.blit(exit_surf, (175, 400))
        screen.blit(text_back, (300 - text_back.get_width() // 2, 325 - text_back.get_height() // 2))
        screen.blit(text_exit, (300 - text_exit.get_width() // 2, 425 - text_exit.get_height() // 2))
        pygame.draw.rect(screen, white, (175, 300, 250, 50), 1)
        pygame.draw.rect(screen, white, (175, 400, 250, 50), 1)
    while True:
        local()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEMOTION:
                if back_rect.collidepoint(i.pos):
                    back_alpha = 100
                    exit_alpha = 0
                elif exit_rect.collidepoint(i.pos):
                    back_alpha = 0
                    exit_alpha = 100
                else:
                    back_alpha = 0
                    exit_alpha = 0
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(i.pos):
                    list_of_nums = []
                    score = old_score = new_score = 0
                    level = 0
                    box_height = 60
                    zero_height = 459
                    line_time_2 = 5  # line time (seconds)
                    line_time_16 = 20
                    num_line = 0  # amount of lines
                    list_of_lines = []
                    list_of_small_rects = []
                    list_of_primes = []
                    list_of_examples = []
                    list_of_status = []
                    col = 0
                    main()
                elif exit_rect.collidepoint(i.pos):
                    sys.exit()

        pygame.display.update()


BackGround = Background('background.jpg', [0,0])

def main():
    global footer, header, num_line, score, zero_height, tread, play
    first_screen()
    tread = threading.Timer(0, func)
    footer = pygame.Surface((600, 80)) # down
    footer.fill(black)
    footer.set_alpha(200)
    header = pygame.Surface((600, 100)) # up
    header.fill(black)
    header.set_alpha(200)
    update_screen()
    draw_new_line()
    pygame.display.update()
    while play:
        clock.tick(FPS)
        check_time()
        if num_line == 8: # max line
            tread.cancel()
            play = False
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                tread.cancel()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    for j in range(len(list_of_small_rects)):
                        for k in range(len(list_of_small_rects[j])):
                            if pygame.Rect(list_of_small_rects[j][k]).collidepoint(i.pos):
                                local_num = list_of_primes[j][k]
                                ind3 = list_of_nums.index(local_num)
                                if ind3 > system - 2:
                                    list_of_primes[j][k] = list_of_nums[0]
                                else:
                                    list_of_primes[j][k] = list_of_nums[ind3 + 1]
                                line_num = count_sum(list_of_primes[j], system)
                    for i in range(num_line):
                        x = check_equal(list_of_primes[i], list_of_examples[i], system)
                        if x:
                            list_of_status[i] = x
                elif i.button == 3:
                    for j in range(len(list_of_small_rects)):
                        for k in range(len(list_of_small_rects[j])):
                            if pygame.Rect(list_of_small_rects[j][k]).collidepoint(i.pos):
                                local_num = list_of_primes[j][k]
                                ind3 = list_of_nums.index(local_num)
                                if ind3 > system - 1:
                                    list_of_primes[j][k] = list_of_nums[0]
                                else:
                                    list_of_primes[j][k] = list_of_nums[ind3 - 1]
                                line_num = count_sum(list_of_primes[j], system)
                    for i in range(num_line):
                        x = check_equal(list_of_primes[i], list_of_examples[i], system)
                        if x:
                            list_of_status[i] = x



        if True in list_of_status:
            ind = list_of_status.index(True)
            list_of_primes.remove(list_of_primes[ind])
            list_of_lines.remove(list_of_lines[ind])
            list_of_examples.remove(list_of_examples[ind])
            list_of_small_rects.remove(list_of_small_rects[ind])
            list_of_status.remove(True)
            num_line -= 1
            score += 100
            zero_height += box_height
            for i in range(ind, len(list_of_small_rects)):
                for j in range(len(list_of_small_rects[i])):
                    list_of_small_rects[i][j] = (list_of_small_rects[i][j][0], list_of_small_rects[i][j][1] + box_height, list_of_small_rects[i][j][2], list_of_small_rects[i][j][3])

        update_screen()
        pygame.display.update()
    last_screen()

main()