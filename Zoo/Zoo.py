print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

camel = r"""
The camel habitat...
a'!   _,,_ a'!   _,,_     a'!   _,,_
  \\_/    \  \\_/    \      \\_/    \.-,
   \, /-( /'-,\, /-( /'-,    \, /-( /
   //\ //\\   //\ //\\       //\ //\\
Look at that!"""
rabbit = r"""
The rabbit habitat...
               ((`\
            ___ \\ '--._
         .'`   `'    o  )
        /    \   '. __.'
       _|    /_  \ \_\_
      {_\______\-'\__\_\"""
Look at that!"""
lion = r"""
      ,''',
         .' ., .',                                  ../'''',
        .'. %%, %.',                            .,/' .,%   :
       .'.% %%%,`%%%'.    .....,,,,,,.....   .,%%% .,%%'. .'
       : %%% %%%%%%',:%%>>%>' .,>>%>>%>%>>%%>,.   `%%%',% :
       : %%%%%%%'.,>>>%'   .,%>%>%'.,>%>%' . `%>>>,. `%%%:'
       ` %%%%'.,>>%'  .,%>>%>%' .,%>%>%' .>>%,. `%%>>,. `%
        `%'.,>>>%'.,%%%%%%%' .,%%>%%>%' >>%%>%>>%.`%% %% `,
        ,`%% %%>>>%%%>>%%>%%>>%>>%>%%%  %%>%%>%%>>%>%%%' % %,
      ,%>%'.>>%>%'%>>%%>%%%%>%'                 `%>%>>%%.`%>>%.
    ,%%>' .>%>%'.%>%>>%%%>>%' ,%%>>%%>%>>%>>%>%%,.`%%%>%%. `%>%.
   ` ,%' .>%%%'.%>%>>%' .,%%%%%%%%'          `%%%%%%.`%%>%% .%%>
   .%>% .%%>' :%>>%%'.,%%%%%%%%%'.%%%%%' `%%%%.`%%%%%.%%%%> %%>%.
  ,%>%' >>%%  >%' `%%%%'     `%%%%%%%'.,>,. `%%%%'     `%%%>>%%>%
.%%>%' .%%>'  %>>%, %% oO ~ Oo %%%>>'.>>>>>>. `% oO ~ Oo'.%%%'%>%,
%>'%> .%>%>%  %%>%%%'  `OoooO'.%%>>'.>>>%>>%>>.`%`OoooO'.%%>% '%>%
%',%' %>%>%'  %>%>%>% .%,>,>,   `>'.>>%>%%>>>%>.`%,>,>' %%%%> .>%>,
` %>% `%>>%%. `%%% %' >%%%%%%>,  ' >>%>>%%%>%>>> >>%%' ,%%>%'.%%>>%.
 .%%'  %%%%>%.   `>%%. %>%%>>>%.>> >>>%>%%%%>%>>.>>>'.>%>%>' %>>%>%%
 `.%%  `%>>%%>    %%>%  %>>>%%%>>'.>%>>>>%%%>>%>>.>',%>>%'  ,>%'>% '
  %>'  %%%%%%'    `%%'  %%%%%> >' >>>>%>>%%>>%>>%> %%>%>' .%>%% .%%
 %>%>, %>%%>>%%,  %>%>% `%%  %>>  >>>%>>>%%>>>>%>>  %%>>,%>%%'.%>%,
%>%>%%, `%>%%>%>%, %>%%> ,%>%>>>.>>`.,.  `"   ..'>.%. % %>%>%'.%>%%;
%'`%%>%  %%>%%  %>% %'.>%>>%>%%>>%::.  `,   /' ,%>>>%>. >%>%'.%>%'%'
` .%>%'  >%%% %>%%'.>%>%;''.,>>%%>%%::.  ..'.,%>>%>%>,`%  %'.>%%' '
  %>%>%% `%>  >%%'.%%>%>>%>%>%>>>%>%>>%,,::,%>>%%>%>>%>%% `>>%>'
  %'`%%>%>>%  %>'.%>>%>%>>;'' ..,,%>%>%%/::%>%%>>%%,,.``% .%>%%
  `    `%>%>>%%' %>%%>>%>>%>%>%>%%>%/'       `%>%%>%>>%%% ' .%'
        %'  `%>% `%>%%;'' .,>>%>%/',;;;;;,;;;;,`%>%>%,`%'   '
        `    `  ` `%>%%%>%%>%%;/ @a;;;;;;;;;;;a@  >%>%%'
                   `/////////';, `@a@@a@@a@@aa@',;`//'
                      `//////.;;,,............,,;;//'
                          `////;;;;;;;;;;;;;;;;;/'
                             `/////////////////'
The lion habitat..."""
deer = r"""
The deer habitat...
(             )
 `--(_   _)--'
      Y-Y
     /@@ \
    /     \
    `--'.  \             ,
        |   `.__________/)
The deer habitat..."""

goose = r"""
                        ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
             hjw    `-'
The goose habitat..."""
bat = r"""
    =/\                 /\=
    / \'._   (\_/)   _.'/ \
   / .''._'--(o.o)--'_.''. \
  /.' _/ |`'=/ " \='`| \_ `.\
 /` .' `\;-,'\___/',-;/` '. '\
/.-' jgs   `\(-V-)/`       `-.\
`            "   "            `
The bat habitat..."""

# Список тварин
animals = ["camel", "lion", "deer", "goose", "bat", "rabbit"]
while True:
    # Введення номера тварини від користувача або команди "exit"
    user_input = input("Please enter the number of the habitat you would like to view (or enter 'exit' to exit): ")

    # Перевірка на вибір команди "exit"
    if user_input.lower() == 'exit':
        break


# Перевірка на правильність введеного числа
    try:
        # Конвертація введеного числа в індекс списку
        index = int(user_input)

        # Вивід тварини за вказаним номером або повідомлення про помилку, якщо номер неправильний
        if 0 <= index < len(animals):
            selected_animal = animals[index]
            if selected_animal == "camel":
                print("The camel habitat...")
                print(camel)
            elif selected_animal == "lion":
                print("The camel habitat...")
                print(lion)
            elif selected_animal == "deer":
                print("The camel habitat...")
                print(deer)
            elif selected_animal == "goose":
                print("The camel habitat...")
                print(goose)
            elif selected_animal == "bat":
                print("The camel habitat...")
                print(bat)
            elif selected_animal == "rabbit":
                print("The camel habitat...")
                print(rabbit)
            else:
                print(f"The {selected_animal} habitat...")
                print("ASCII art or description of the habitat can be placed here.")
        else:
            print("Invalid habitat number.")
    except ValueError:
        print("Please enter a valid number.")

    # Завершення програми
    print("You've reached the end of the program.")
