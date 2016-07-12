class PokeGuesser():
    def __init__(self):
        self.pokedex = dict()
        self._populate_pokemon()

    def guess_pokemon(self, pokemon_line, evolve, candy):
        """using the pokemon line, and the evolve data,
        attempt to guess which pokemon is being displayed"""

        pokemon_line = pokemon_line if pokemon_line else ""
        evolve = True if evolve else False
        candy = candy if candy else 0

        for pokemon_number, data in self.pokedex.items():
            if data['evolve'] is evolve and data['line'] == pokemon_line:
                try:
                    if data['stage'] < 3 or evolve is False:
                        return data['pokemon']
                    elif int(candy) == data['candy']: # 3 stage pokemon, candy matches
                                return data['pokemon']
                except KeyError:
                    continue

    def _populate_pokemon(self):
        self.pokedex[1] = {'pokemon': 'Bulbasaur', 'evolve': True, 'line': 'BULBASAUR', 'stage': 3, 'candy': 25}
        self.pokedex[2] = {'pokemon': 'Ivysaur', 'evolve': True, 'line': 'BULBASAUR', 'stage': 3, 'candy': 100}
        self.pokedex[3] = {'pokemon': 'Venusaur', 'evolve': False, 'line': 'BULBASAUR', 'stage': 3}
        self.pokedex[4] = {'pokemon': 'Charmander', 'evolve': True, 'line': 'CHARMANDER', 'stage': 3, 'candy': 25}
        self.pokedex[5] = {'pokemon': 'Charmeleon', 'evolve': True, 'line': 'CHARMANDER', 'stage': 3, 'candy': 100}
        self.pokedex[6] = {'pokemon': 'Charizard', 'evolve': False, 'line': 'CHARMANDER', 'stage': 3}
        self.pokedex[7] = {'pokemon': 'Squirtle', 'evolve': True, 'line': 'SQUIRTLE', 'stage': 3, 'candy': 25}
        self.pokedex[8] = {'pokemon': 'Wartortle', 'evolve': True, 'line': 'SQUIRTLE', 'stage': 3, 'candy': 100}
        self.pokedex[9] = {'pokemon': 'Blastoise', 'evolve': False, 'line': 'SQUIRTLE', 'stage': 3}
        self.pokedex[10] = {'pokemon': 'Caterpie', 'evolve': True, 'line': 'CATERPIE', 'stage': 3, 'candy': 25}
        self.pokedex[11] = {'pokemon': 'Metapod', 'evolve': True, 'line': 'CATERPIE', 'stage': 3, 'candy': 100}
        self.pokedex[12] = {'pokemon': 'Butterfree', 'evolve': False, 'line': 'CATERPIE', 'stage': 3}
        self.pokedex[13] = {'pokemon': 'Weedle', 'evolve': True, 'line': 'WEEDLE', 'stage': 3, 'candy': 25}
        self.pokedex[14] = {'pokemon': 'Kakuna', 'evolve': True, 'line': 'WEEDLE', 'stage': 3, 'candy': 100}
        self.pokedex[15] = {'pokemon': 'Beedrill', 'evolve': False, 'line': 'WEEDLE', 'stage': 3}
        self.pokedex[16] = {'pokemon': 'Pidgey', 'evolve': True, 'line': 'PIDGEY', 'stage': 3, 'candy': 25}
        self.pokedex[17] = {'pokemon': 'Pidgeotto', 'evolve': True, 'line': 'PIDGEY', 'stage': 3, 'candy': 100}
        self.pokedex[18] = {'pokemon': 'Pidgeot', 'evolve': False, 'line': 'PIDGEY', 'stage': 3}
        self.pokedex[19] = {'pokemon': 'Rattata', 'evolve': True, 'line': 'RATTATA', 'stage': 2, 'candy': 50}
        self.pokedex[20] = {'pokemon': 'Ratticate', 'evolve': False, 'line': 'RATTATA', 'stage': 2}
        self.pokedex[21] = {'pokemon': 'Spearow', 'evolve': True, 'line': 'SPEAROW', 'stage': 2, 'candy': 50}
        self.pokedex[22] = {'pokemon': 'Fearow', 'evolve': False, 'line': 'SPEAROW', 'stage': 2}
        self.pokedex[23] = {'pokemon': 'Ekans', 'evolve': True, 'line': 'EKANS', 'stage': 2, 'candy': 50}
        self.pokedex[24] = {'pokemon': 'Arbok', 'evolve': False, 'line': 'EKANS', 'stage': 2}
        self.pokedex[25] = {'pokemon': 'Pikachu', 'evolve': True, 'line': 'PIKACHU', 'stage': 2, 'candy': 50}
        self.pokedex[26] = {'pokemon': 'Raichu', 'evolve': False, 'line': 'PIKACHU', 'stage': 2}
        self.pokedex[27] = {'pokemon': 'Sandshrew', 'evolve': True, 'line': 'SANDSHREW', 'stage': 2, 'candy': 50}
        self.pokedex[28] = {'pokemon': 'Sandslash', 'evolve': False, 'line': 'SANDSHREW', 'stage': 2}
        self.pokedex[29] = {'pokemon': 'Nidoran', 'evolve': True, 'line': 'NIDORAN', 'stage': 3, 'candy': 25}
        self.pokedex[30] = {'pokemon': 'Nidorina', 'evolve': True, 'line': 'NIDORAN', 'stage': 3, 'candy': 100}
        self.pokedex[31] = {'pokemon': 'Nidoqueen', 'evolve': False, 'line': 'NIDORAN', 'stage': 3}
        self.pokedex[32] = {'pokemon': 'Nidoran', 'evolve': True, 'line': 'NIDORAN', 'stage': 3, 'candy': 25}
        self.pokedex[33] = {'pokemon': 'Nidorino', 'evolve': True, 'line': 'NIDORAN', 'stage': 3, 'candy': 100}
        self.pokedex[34] = {'pokemon': 'Nidoking', 'evolve': False, 'line': 'NIDORAN', 'stage': 3}
        self.pokedex[35] = {'pokemon': 'Clefairy', 'evolve': True, 'line': 'CLEFAIRY', 'stage': 2, 'candy': 50}
        self.pokedex[36] = {'pokemon': 'Clefable', 'evolve': False, 'line': 'CLEFAIRY', 'stage': 2}
        self.pokedex[37] = {'pokemon': 'Vulpix', 'evolve': True, 'line': 'VULPIX', 'stage': 2, 'candy': 50}
        self.pokedex[38] = {'pokemon': 'Ninetails', 'evolve': False, 'line': 'VULPIX', 'stage': 2}
        self.pokedex[39] = {'pokemon': 'Jigglypuff', 'evolve': True, 'line': 'JIGGLYPUFF', 'stage': 2, 'candy': 50}
        self.pokedex[40] = {'pokemon': 'Wigglytuff', 'evolve': False, 'line': 'JIGGLYPUFF', 'stage': 2}
        self.pokedex[41] = {'pokemon': 'Zubat', 'evolve': True, 'line': 'ZUBAT', 'stage': 2, 'candy': 50}
        self.pokedex[42] = {'pokemon': 'Golbat', 'evolve': False, 'line': 'ZUBAT', 'stage': 2}
        self.pokedex[43] = {'pokemon': 'Oddish', 'evolve': True, 'line': 'ODDISH', 'stage': 3, 'candy': 25}
        self.pokedex[44] = {'pokemon': 'Gloom', 'evolve': True, 'line': 'ODDISH', 'stage': 3, 'candy': 100}
        self.pokedex[45] = {'pokemon': 'Vileplume', 'evolve': False, 'line': 'ODDISH', 'stage': 3}
        self.pokedex[46] = {'pokemon': 'Paras', 'evolve': True, 'line': 'PARAS', 'stage': 2, 'candy': 50}
        self.pokedex[47] = {'pokemon': 'Parasect', 'evolve': False, 'line': 'PARAS', 'stage': 2}
        self.pokedex[48] = {'pokemon': 'Venomat', 'evolve': True, 'line': 'VENONAT', 'stage': 2, 'candy': 50}
        self.pokedex[49] = {'pokemon': 'Venomoth', 'evolve': False, 'line': 'VENONAT', 'stage': 2}
        self.pokedex[50] = {'pokemon': 'Diglett', 'evolve': True, 'line': 'DIGLETT', 'stage': 2, 'candy': 50}
        self.pokedex[51] = {'pokemon': 'Dugtrio', 'evolve': False, 'line': 'DIGLETT', 'stage': 2}
        self.pokedex[52] = {'pokemon': 'Meowth', 'evolve': True, 'line': 'MEOWTH', 'stage': 2, 'candy': 50}
        self.pokedex[53] = {'pokemon': 'Persian', 'evolve': False, 'line': 'MEOWTH', 'stage': 2}
        self.pokedex[54] = {'pokemon': 'Psyduck', 'evolve': True, 'line': 'PSYDUCK', 'stage': 2, 'candy': 50}
        self.pokedex[55] = {'pokemon': 'Golduck', 'evolve': False, 'line': 'PSYDUCK', 'stage': 2}
        self.pokedex[56] = {'pokemon': 'Mankey', 'evolve': True, 'line': 'MANKEY', 'stage': 2, 'candy': 50}
        self.pokedex[57] = {'pokemon': 'Primeape', 'evolve': False, 'line': 'MANKEY', 'stage': 2}
        self.pokedex[58] = {'pokemon': 'Growlithe', 'evolve': True, 'line': 'GROWLITHE', 'stage': 2, 'candy': 50}
        self.pokedex[59] = {'pokemon': 'Arcanine', 'evolve': False, 'line': 'GROWLITHE', 'stage': 2}
        self.pokedex[60] = {'pokemon': 'Poliwag', 'evolve': True, 'line': 'POLIWAG', 'stage': 3, 'candy': 25}
        self.pokedex[61] = {'pokemon': 'Poliwhirl', 'evolve': True, 'line': 'POLIWAG', 'stage': 3, 'candy': 100}
        self.pokedex[62] = {'pokemon': 'Poliwrath', 'evolve': False, 'line': 'POLIWAG', 'stage': 3}
        self.pokedex[63] = {'pokemon': 'Abra', 'evolve': True, 'line': 'ABRA', 'stage': 3, 'candy': 25}
        self.pokedex[64] = {'pokemon': 'Kadabra', 'evolve': True, 'line': 'ABRA', 'stage': 3, 'candy': 100}
        self.pokedex[65] = {'pokemon': 'Alakazam', 'evolve': False, 'line': 'ABRA', 'stage': 3}
        self.pokedex[66] = {'pokemon': 'Machop', 'evolve': True, 'line': 'MACHOP', 'stage': 3, 'candy': 25}
        self.pokedex[67] = {'pokemon': 'Machoke', 'evolve': True, 'line': 'MACHOP', 'stage': 3, 'candy': 100}
        self.pokedex[68] = {'pokemon': 'Machamp', 'evolve': False, 'line': 'MACHOP', 'stage': 3}
        self.pokedex[69] = {'pokemon': 'Bellsprout', 'evolve': True, 'line': 'BELLSPROUT', 'stage': 3, 'candy': 25}
        self.pokedex[70] = {'pokemon': 'Weepinbell', 'evolve': True, 'line': 'BELLSPROUT', 'stage': 3, 'candy': 100}
        self.pokedex[71] = {'pokemon': 'Victreebel', 'evolve': False, 'line': 'BELLSPROUT', 'stage': 3}
        self.pokedex[72] = {'pokemon': 'Tentacool', 'evolve': True, 'line': 'TENTACOOL', 'stage': 2, 'candy': 50}
        self.pokedex[73] = {'pokemon': 'Tentacruel', 'evolve': False, 'line': 'TENTACOOL', 'stage': 2}
        self.pokedex[74] = {'pokemon': 'Geodude', 'evolve': True, 'line': 'GEODUDE', 'stage': 3, 'candy': 25}
        self.pokedex[75] = {'pokemon': 'Graveler', 'evolve': True, 'line': 'GEODUDE', 'stage': 3, 'candy': 100}
        self.pokedex[76] = {'pokemon': 'Golem', 'evolve': False, 'line': 'GEODUDE', 'stage': 3}
        self.pokedex[77] = {'pokemon': 'Ponyta', 'evolve': True, 'line': 'PONYTA', 'stage': 2, 'candy': 50}
        self.pokedex[78] = {'pokemon': 'Rapidash', 'evolve': False, 'line': 'PONYTA', 'stage': 2}
        self.pokedex[79] = {'pokemon': 'Slowpoke', 'evolve': True, 'line': 'SLOWPOKE', 'stage': 2, 'candy': 50}
        self.pokedex[80] = {'pokemon': 'Slowbro', 'evolve': False, 'line': 'SLOWPOKE', 'stage': 2}
        self.pokedex[81] = {'pokemon': 'Magnemite', 'evolve': True, 'line': 'MAGNEMITE', 'stage': 2, 'candy': 50}
        self.pokedex[82] = {'pokemon': 'Magneton', 'evolve': False, 'line': 'MAGNEMITE', 'stage': 2}
        self.pokedex[83] = {'pokemon': 'Farfetch\'d', 'evolve': False, 'line': 'FARFETCH\'D', 'stage': 1}
        self.pokedex[84] = {'pokemon': 'Doduo', 'evolve': True, 'line': 'DODUO', 'stage': 2, 'candy': 50}
        self.pokedex[85] = {'pokemon': 'Dodrio', 'evolve': False, 'line': 'DODUO', 'stage': 2}
        self.pokedex[86] = {'pokemon': 'Seel', 'evolve': True, 'line': 'SEEL', 'stage': 2, 'candy': 50}
        self.pokedex[87] = {'pokemon': 'Dewgong', 'evolve': False, 'line': 'SEEL', 'stage': 2}
        self.pokedex[88] = {'pokemon': 'Grimer', 'evolve': True, 'line': 'GRIMER', 'stage': 2, 'candy': 50}
        self.pokedex[89] = {'pokemon': 'Muk', 'evolve': False, 'line': 'GRIMER', 'stage': 2}
        self.pokedex[90] = {'pokemon': 'Shellder', 'evolve': True, 'line': 'SHELLDER', 'stage': 2, 'candy': 50}
        self.pokedex[91] = {'pokemon': 'Cloyster', 'evolve': False, 'line': 'SHELLDER', 'stage': 2}
        self.pokedex[92] = {'pokemon': 'Gastly', 'evolve': True, 'line': 'GASTLY', 'stage': 3, 'candy': 25}
        self.pokedex[93] = {'pokemon': 'Haunter', 'evolve': True, 'line': 'GASTLY', 'stage': 3, 'candy': 100}
        self.pokedex[94] = {'pokemon': 'Gengar', 'evolve': False, 'line': 'GASTLY', 'stage': 3}
        self.pokedex[95] = {'pokemon': 'Onix', 'evolve': False, 'line': 'ONIX', 'stage': 1}
        self.pokedex[96] = {'pokemon': 'Drowzee', 'evolve': True, 'line': 'DROWZEE', 'stage': 2, 'candy': 50}
        self.pokedex[97] = {'pokemon': 'Hypno', 'evolve': False, 'line': 'DROWZEE', 'stage': 2}
        self.pokedex[98] = {'pokemon': 'Krabby', 'evolve': True, 'line': 'KRABBY', 'stage': 2, 'candy': 50}
        self.pokedex[99] = {'pokemon': 'Kingler', 'evolve': False, 'line': 'KRABBY', 'stage': 2}
        self.pokedex[100] = {'pokemon': 'Voltorb', 'evolve': True, 'line': 'VOLTORB', 'stage': 2, 'candy': 50}
        self.pokedex[101] = {'pokemon': 'Electrode', 'evolve': False, 'line': 'VOLTORB', 'stage': 2}
        self.pokedex[102] = {'pokemon': 'Exeggcute', 'evolve': True, 'line': 'EXEGGCUTE', 'stage': 2, 'candy': 50}
        self.pokedex[103] = {'pokemon': 'Exeggutor', 'evolve': False, 'line': 'EXEGGCUTE', 'stage': 2}
        self.pokedex[104] = {'pokemon': 'Cubone', 'evolve': True, 'line': 'CUBONE', 'stage': 2, 'candy': 50}
        self.pokedex[105] = {'pokemon': 'Marowak', 'evolve': False, 'line': 'CUBONE', 'stage': 2}
        self.pokedex[106] = {'pokemon': 'Hitmonlee', 'evolve': False, 'line': 'HITMONLEE', 'stage': 1}
        self.pokedex[107] = {'pokemon': 'Hitmonchan', 'evolve': False, 'line': 'HITMONCHAN', 'stage': 1}
        self.pokedex[108] = {'pokemon': 'Lickitung', 'evolve': False, 'line': 'LICKITUNG', 'stage': 1}
        self.pokedex[109] = {'pokemon': 'Koffing', 'evolve': True, 'line': 'KOFFING', 'stage': 2, 'candy': 50}
        self.pokedex[110] = {'pokemon': 'Wheezing', 'evolve': False, 'line': 'KOFFING', 'stage': 2}
        self.pokedex[111] = {'pokemon': 'Rhyhorn', 'evolve': True, 'line': 'RHYHORN', 'stage': 2, 'candy': 50}
        self.pokedex[112] = {'pokemon': 'Rhydon', 'evolve': False, 'line': 'RHYHORN', 'stage': 2}
        self.pokedex[113] = {'pokemon': 'Chansey', 'evolve': False, 'line': 'CHANSEY', 'stage': 1}
        self.pokedex[114] = {'pokemon': 'Tangela', 'evolve': False, 'line': 'TANGELA', 'stage': 1}
        self.pokedex[115] = {'pokemon': 'Kangaskhan', 'evolve': False, 'line': 'KANGASKHAN', 'stage': 1}
        self.pokedex[116] = {'pokemon': 'Horsea', 'evolve': True, 'line': 'HORSEA', 'stage': 2, 'candy': 50}
        self.pokedex[117] = {'pokemon': 'Seadra', 'evolve': False, 'line': 'HORSEA', 'stage': 2}
        self.pokedex[118] = {'pokemon': 'Goldeen', 'evolve': True, 'line': 'GOLDEEN', 'stage': 2, 'candy': 50}
        self.pokedex[119] = {'pokemon': 'Seaking', 'evolve': False, 'line': 'GOLDEEN', 'stage': 2}
        self.pokedex[120] = {'pokemon': 'Staryu', 'evolve': True, 'line': 'STARYU', 'stage': 2, 'candy': 50}
        self.pokedex[121] = {'pokemon': 'Starmie', 'evolve': False, 'line': 'STARYU', 'stage': 2}
        self.pokedex[122] = {'pokemon': 'Mr. Mime', 'evolve': False, 'line': 'MR. MIME', 'stage': 1}
        self.pokedex[123] = {'pokemon': 'Scyther', 'evolve': False, 'line': 'SCYTHER', 'stage': 1}
        self.pokedex[124] = {'pokemon': 'Jynx', 'evolve': False, 'line': 'JYNX', 'stage': 1}
        self.pokedex[125] = {'pokemon': 'Electrabuzz', 'evolve': False, 'line': 'ELECTRABUZZ', 'stage': 1}
        self.pokedex[126] = {'pokemon': 'Magmar', 'evolve': False, 'line': 'MAGMAR', 'stage': 1}
        self.pokedex[127] = {'pokemon': 'Pinsir', 'evolve': False, 'line': 'PINSIR', 'stage': 1}
        self.pokedex[128] = {'pokemon': 'Tauros', 'evolve': False, 'line': 'TAUROS', 'stage': 1}
        self.pokedex[129] = {'pokemon': 'Magikarp', 'evolve': True, 'line': 'MAGIKARP', 'stage': 2, 'candy': 400}
        self.pokedex[130] = {'pokemon': 'Gyarados', 'evolve': False, 'line': 'MAGIKARP', 'stage': 2}
        self.pokedex[131] = {'pokemon': 'Lapras', 'evolve': False, 'line': 'LAPRAS', 'stage': 1}
        self.pokedex[132] = {'pokemon': 'Ditto', 'evolve': False, 'line': 'DITTO', 'stage': 1}
        self.pokedex[133] = {'pokemon': 'Eevee', 'evolve': True, 'line': 'EEVEE', 'stage': 3, 'candy': 25}
        self.pokedex[134] = {'pokemon': 'Vaporeon', 'evolve': False, 'line': 'EEVEE', 'stage': 3}
        self.pokedex[135] = {'pokemon': 'Jolteon', 'evolve': False, 'line': 'EEVEE', 'stage': 3}
        self.pokedex[136] = {'pokemon': 'Flareon', 'evolve': False, 'line': 'EEVEE', 'stage': 3}
        self.pokedex[137] = {'pokemon': 'Porygon', 'evolve': False, 'line': 'PORYGON', 'stage': 1}
        self.pokedex[138] = {'pokemon': 'Omanyte', 'evolve': True, 'line': 'OMANYTE', 'stage': 2, 'candy': 50}
        self.pokedex[139] = {'pokemon': 'Omastar', 'evolve': False, 'line': 'OMANYTE', 'stage': 2}
        self.pokedex[140] = {'pokemon': 'Kabuto', 'evolve': True, 'line': 'KABUTO', 'stage': 2, 'candy': 50}
        self.pokedex[141] = {'pokemon': 'Kabutops', 'evolve': False, 'line': 'KABUTO', 'stage': 2}
        self.pokedex[142] = {'pokemon': 'Aerodactyl', 'evolve': False, 'line': 'AERODACTYL', 'stage': 1}
        self.pokedex[143] = {'pokemon': 'Snorlax', 'evolve': False, 'line': 'SNORLAX', 'stage': 1}
        self.pokedex[144] = {'pokemon': 'Articuno', 'evolve': False, 'line': 'ARTICUNO', 'stage': 1}
        self.pokedex[145] = {'pokemon': 'Zapdos', 'evolve': False, 'line': 'ZAPDOS', 'stage': 1}
        self.pokedex[146] = {'pokemon': 'Moltres', 'evolve': False, 'line': 'MOLTRES', 'stage': 1}
        self.pokedex[147] = {'pokemon': 'Dratini', 'evolve': True, 'line': 'DRATINI', 'stage': 3, 'candy': 25}
        self.pokedex[148] = {'pokemon': 'Dragonair', 'evolve': True, 'line': 'DRATINI', 'stage': 3, 'candy': 100}
        self.pokedex[149] = {'pokemon': 'Dragonite', 'evolve': False, 'line': 'DRATINI', 'stage': 3}
        self.pokedex[150] = {'pokemon': 'Mewtwo', 'evolve': False, 'line': 'MEWTWO', 'stage': 1}
        self.pokedex[151] = {'pokemon': 'Mew', 'evolve': False, 'line': 'MEW', 'stage': 1}
