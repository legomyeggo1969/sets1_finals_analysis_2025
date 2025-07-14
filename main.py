import time
import enum
import matplotlib.pyplot as plt

class TicketType(enum.Enum):
    Cap = 0
    Bleed = 1
    Infantry = 2
    Vehicle = 3
    RadioLoss = 4

def main():

    for label, filename, ingame_match_duration in [
            ('EnR v OC - Round 1', 'data/enroc_r1.log', 48*60 + 4),
            ('EnR v OC - Round 2', 'data/enroc_r2.log', 50*60 + 45),
            ('82 v OWLS - Round 1', 'data/82owls_r1.log', 35*60 + 7),
            ('82 v OWLS - Round 2', 'data/82owls_r2.log', 33*60 + 49),
            ]:
        for excursion in [1]:
            if 'enroc' in filename:
                team_names = ['enr', 'oc']
            else:
                team_names = ['82team', 'owls']
            mr = MatchRound(
                ticket_count_start=250,
                ingame_match_start=64*60,
                ingame_staging_end=60*60,
                ingame_match_duration=ingame_match_duration,
                team_names=team_names,
                )
            mr.add_commander_player('enr', 'Zeus Koala')
            mr.add_commander_player('oc', 'Arkantdos')
            mr.add_commander_player('owls', 'NOOB132d')
            mr.add_commander_player('82team', 'Nukuatuk')
            
            # CAF - side 1
            # PLAGF - side 2
            if '82owls_r1' in filename:
                mr.set_team_side('owls', 1)
                mr.set_team_side('82team', 2)
            elif '82owls_r2' in filename:
                mr.set_team_side('82team', 1)
                mr.set_team_side('owls', 2)
            elif 'enroc_r1' in filename:
                mr.set_team_side('oc', 1)
                mr.set_team_side('enr', 2)
            elif 'enroc_r2' in filename:
                mr.set_team_side('enr', 1)
                mr.set_team_side('oc', 2)
            else:
                raise ValueError(f'Unknown team sides for {filename}')


            slr = SquadLogReader()
            slr.register_search(mr.log_game_state, 'LogGameState', 'Match State Changed')
            slr.register_search(mr.log_player_die, 'LogSquadTrace', 'Die():')
            slr.register_search(mr.log_vic_damage, 'LogSquadTrace', 'TraceAndMessageClient():')
            print('*'*80)
            print('*', filename)
            print('*'*80)
            slr.search_tick_group(filename)

            if 'enroc_r1' in filename:
                mr.delta_ticket_count_ingame('55:21',          'enr', 30, TicketType.Cap) # finish lower orchard cap
                mr.delta_ticket_count_ingame('54:41',          'oc',  30, TicketType.Cap) # finish hemp cap
                mr.delta_ticket_count_ingame('52:15',          'enr', 30, TicketType.Cap) # finish radio cap
                mr.add_ticket_bleed_ingame(  '52:15', '18:19', 'oc', -1) # mid cap bleed
                mr.delta_ticket_count_ingame('41:43',          'enr', -10, TicketType.Vehicle) # ZBL loss based on logs
                # [2025.07.13-18.25.34:363][576] JamesEZ was the driver and log showed the loss as the driver
            elif 'enroc_r2' in filename:
                mr.delta_ticket_count_ingame('55:13',          'oc',  30, TicketType.Cap) # finish lower orchard cap
                mr.delta_ticket_count_ingame('55:36',          'enr', 30, TicketType.Cap) # finish hemp cap
                mr.delta_ticket_count_ingame('51:50',          'enr', 30, TicketType.Cap) # finish radio cap
                mr.add_ticket_bleed_ingame(  '51:50', '18:23', 'oc', -1) # mid cap bleed until neutral
                mr.delta_ticket_count_ingame('20:41',          'oc', -10, TicketType.Vehicle) # ZBL loss based on stream (@06:19:38)
                mr.delta_ticket_count_ingame('16:15',          'oc',  60, TicketType.Cap) # flip radio cap
                mr.delta_ticket_count_ingame('16:15',          'enr',-30, TicketType.Cap) # flip radio cap
                mr.add_ticket_bleed_ingame(  '16:15', '00:00', 'enr', -1) # mid cap bleed until neutral
                mr.delta_ticket_count_ingame('15:31',          'enr', -10, TicketType.Vehicle) # LAV loss based on stream (@06:24:23)
            elif '82owls_r1' in filename:
                mr.delta_ticket_count_ingame('54:29',          '82team', 30, TicketType.Cap) # finish lower orchard cap
                mr.delta_ticket_count_ingame('51:08',          '82team', 30, TicketType.Cap) # finish radio cap
                mr.add_ticket_bleed_ingame(  '51:08', '00:00', 'owls', -1) # mid cap bleed
                mr.delta_ticket_count_ingame('50:51',          'owls',  30, TicketType.Cap) # finish hemp cap
                mr.delta_ticket_count_ingame('42:01',          'owls', -10, TicketType.Vehicle) # based on stream (@1:05:40)
                mr.delta_ticket_count_ingame('36:49',          'owls', -20, TicketType.RadioLoss) # based on stream (@1:10:53)
            elif '82owls_r2' in filename:
                mr.delta_ticket_count_ingame('53:28',          'owls',  30, TicketType.Cap) # finish lower orchard cap (based on stream)
                mr.delta_ticket_count_ingame('54:40',          '82team', 30, TicketType.Cap) # finish hemp cap (based on stream @1:40:42)
                mr.delta_ticket_count_ingame('41:05',          '82team', 30, TicketType.Cap) # finish radio cap
                mr.add_ticket_bleed_ingame(  '41:05', '00:00', 'owls', -1) # mid cap bleed
                mr.delta_ticket_count_ingame('39:54',          'owls', -10, TicketType.Vehicle) # ZBL loss based on stream (@1:53:31)
            mr.show(f'{label}')
    import pdb; pdb.set_trace()
    

################################################################################
def infer_side_from_player_name(player_name):
    pn = player_name.lower()
    team = None
    if pn == 'nullptr':
        pass
    elif 'enr' in pn:
        team = 'enr'
    elif '[oc]' in pn:
        team = 'oc'
    elif '[owl]' in pn:
        team = 'owls'
    elif 'o.w.l.s' in pn:
        team = 'owls'
    elif pn.startswith('82'):
        team = '82team'
    elif 'sergey andreevich' in pn:
        team = '82team'
    elif 'bogdan' in pn:
        team = '82team'
    elif 'boggdan' in pn:
        team = '82team'
    elif 'trevor' in pn:
        team = '82team'
    elif 'legendary kr1nyx' in pn:
        team = '82team'
    elif '0:5:0' in pn:
        team = '82team'
    elif '0-8-0' in pn:
        team = '82team'
    elif pn == 'ren':
        team = '82team'
    elif pn == 'sso  ren':
        team = '82team'
    else:
        print(f'WARNING: could not infer team from player name: {player_name}')
        import pdb; pdb.set_trace()
    return team

def vehicle_side_and_ticket_costs(vic_name):
    vn = vic_name.lower()
    if 'luvw_m2_desert' in vn:
        return 1, 5
    if 'caf_util_desert' in vn:
        return 1, 5
    if 'lav6_desert' in vn:
        return 1, 10
    if 'zbl08' in vn:
        return 2, 10
    if 'csk131' in vn:
        return 2, 5
    if 'ctm131' in vn:
        return 2, 5
    raise ValueError(f'Unknown vehicle name: {vic_name}')

################################################################################
class MatchRound:
    def __init__(self,
                 ticket_count_start,
                 ingame_match_start,
                 ingame_staging_end,
                 ingame_match_duration,
                 team_names):
        self.time_start = None
        self.time_end = None
        self.ticket_count_start = ticket_count_start
        self.ingame_match_start = ingame_match_start
        self.ingame_staging_end = ingame_staging_end
        self.ingame_match_duration = ingame_match_duration
        self.commander_player_names = dict()
        self.team_side = dict()
        self.ticket_count = dict()
        for team_name in team_names:
            self.ticket_count[team_name] = []
        self.ticket_bleed = dict()
    
    def set_team_side(self, team_name, side):
        self.team_side[side] = team_name

    def add_commander_player(self, team_name, player_name):
        self.commander_player_names.setdefault(team_name, set()).add(player_name.lower())

    def delta_ticket_count(self, t_now, team_name, ticket_count, ticket_type):
        self.ticket_count[team_name].append((t_now, ticket_count, ticket_type))
    
    def delta_ticket_count_ingame(self, t_ingame, team_name, ticket_count, ticket_type):
        t_ingame = self._igt(t_ingame)
        t_now = self.time_start + ((self.ingame_match_start - t_ingame) * self.get_time_scale_factor())
        self.ticket_count[team_name].append((t_now, ticket_count, ticket_type))

    def _igt(self, time_string):
        """Convert ingame time string to seconds."""
        parts = time_string.split(':')
        if len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        elif len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        else:
            raise ValueError(f'Invalid ingame time format: {time_string}')

    def add_ticket_bleed_ingame(self, t_start_ingame, t_end_ingame, team_name, ticket_count_per_min):
        t_start_ingame = self._igt(t_start_ingame)
        t_end_ingame = self._igt(t_end_ingame)
        t_start = self.time_start + ((self.ingame_match_start - t_start_ingame) * self.get_time_scale_factor())
        t_end = self.time_start + ((self.ingame_match_start - t_end_ingame) * self.get_time_scale_factor())
        self.ticket_bleed.setdefault(team_name, []).append((t_start, t_end, abs(ticket_count_per_min)))


    def log_game_state(self, tg_time, matched_content, tg_content):
        for line in matched_content:
            if 'to InProgress' in line:
                self.time_start = time.mktime(tg_time)
            elif 'to WaitingPostMatch' in line:
                self.time_end = time.mktime(tg_time)


    def log_vic_damage(self, tg_time, matched_content, tg_content):
        for line in matched_content:
            if 'health remaining -' not in line:
                continue
            ix_vic_name_start = 42
            vic_name = line[ix_vic_name_start:].split(':')[0]
            if not vic_name.startswith('BP_'):
                continue
            t_now = time.mktime(tg_time)
            vic_side, ticket_amount = vehicle_side_and_ticket_costs(vic_name)
            vic_team = self.team_side[vic_side]
            self.delta_ticket_count(t_now, vic_team, -abs(ticket_amount), TicketType.Vehicle)
            print('\tVIC LOSS\t', t_now, vic_team, -ticket_amount, vic_name)
    

    def log_player_die(self, tg_time, matched_content, tg_content):
        for line in matched_content:
            t_now = time.mktime(tg_time)
            ix_vic_name_start = line.find('Die(): Player:')+14
            ix_vic_name_end = line.find('KillingDamage=')
            vic_name = line[ix_vic_name_start:ix_vic_name_end].strip()
            vic_team = infer_side_from_player_name(vic_name)
            if vic_team is None:
                print(f'WARNING: could not infer team from player name: {vic_name}')
                continue
            #import pdb; pdb.set_trace()
            #print(f'dt={t_now - self.time_start}\t[{vic_team}:{vic_name}]\t{line}')
            
            ticket_amount = -1
            commanders = self.commander_player_names.get(vic_team, set())
            for cmdr in commanders:
                if cmdr.lower() in vic_name.lower():
                    ticket_amount = -2
                    #print(f'Commander {vic_name} died, removing 2 tickets')
                    break
            self.delta_ticket_count(t_now, vic_team, ticket_amount, TicketType.Infantry)

    def get_time_scale_factor(self):
        return (self.time_end - self.time_start) / self.ingame_match_duration

    def to_ingame_time(self, time_of_interest):
        assert(self.time_start <= time_of_interest)
        t = self.ingame_match_start - (time_of_interest - self.time_start) * self.get_time_scale_factor()
        return t/60

    def show(self, label, show_timeline_data=False):
        server_log_duration = self.time_end - self.time_start
        ingame_duration = self.ingame_match_duration
        time_scale_factor = server_log_duration / ingame_duration
        print('Match Start:', self.time_start)
        print('Match End:', self.time_end)
        print('Match Duration:', server_log_duration, 'seconds')
        print('Match Time Scale Factor:', time_scale_factor)

        # Add ticket bleeds
        for team_name, bleeds in self.ticket_bleed.items():
            for t_start, t_end, ticket_count_per_min in bleeds:
                t_now = t_start
                t_step = 60 / ticket_count_per_min
                while t_now < t_end and t_now < self.time_end:
                    self.delta_ticket_count(t_now, team_name, -1, TicketType.Bleed)
                    t_now += t_step

        f = plt.figure(figsize=(12, 6))
        ax = f.add_subplot(1,1,1)
        if self.time_start is not None:
            ax.axvline(x=self.to_ingame_time(self.time_start), color='green', linestyle='--', label='Match Start')
        if self.ingame_staging_end is not None:
            ax.axvline(x=self.to_ingame_time(self.time_start+4*60), color='green', linestyle='--', label='Staging End')
        if self.time_end is not None:
            ax.axvline(x=self.to_ingame_time(self.time_end), color='red', linestyle='--', label='Match End')
        team_ticket_summary = dict()
        for team_name, ticket_count in self.ticket_count.items():
            ticket_count.sort()
            tickets = self.ticket_count_start
            line = [(self.to_ingame_time(self.time_start), tickets)]
            ticket_type = dict()
            team_ticket_summary[team_name] = ticket_type
            for t, dt, t_type in ticket_count:
                ticket_type[t_type] = ticket_type.get(t_type, 0) + dt
                prior_t, prior_ticket = line[-1]
                if prior_t < t - 1:
                    line.append((self.to_ingame_time(t-1), prior_ticket))
                tickets += dt
                if show_timeline_data:
                    print(f'{team_name} {t} {dt} {t_type.name} tickets={tickets}')
                line.append((self.to_ingame_time(t), tickets))
                max_tickets = max(300, max([tix for __, tix in line]))
            ax.plot([t[0] for t in line], [t[1] for t in line], label=team_name)
            label = f'{label} | {team_name}={tickets}'

        for team_name, ticket_type in team_ticket_summary.items():
            for t_type, tix in ticket_type.items():
                print(f'- {team_name} {t_type.name}={tix}')
        ax.set_xlabel('In-Game Time (minutes)')
        ax.invert_xaxis()
        ax.set_xlim(self.to_ingame_time(self.time_start), 0)
        ax.set_ylim(0, max_tickets)
        ax.set_title(label)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        plt.legend()
        plt.show(block=False)
        filename = label.replace(' ', '_').replace('|', '_').replace(':', '-')
        f.savefig(f'output/{filename}.png',dpi=300)


################################################################################
class SquadLogReader:
    def __init__(self):
        pass
        self.searches = {}

    def register_search(self, func_callback, search_type, *search_strings):
        k = search_type, search_strings
        self.searches.setdefault(k, []).append(func_callback)


    def search_tick_group(self, filename, tick_callback_func=None):
        prior_tg_tick = 0
        for tg_tick, tg_time, tg_types, tg_content in read_log_raw_tick_group(filename):
            if tg_tick < prior_tg_tick:
                if callable(tick_callback_func):
                    tick_callback_func()

            prior_tg_tick = tg_tick
            for (search_type, search_strings), callbacks in self.searches.items():
                if search_type in tg_types:
                    matched = [content for logtype, content in tg_content if logtype == search_type and all(ss in content for ss in search_strings)]
                    if matched:
                        for func_cb in callbacks:
                            func_cb(tg_time, matched, tg_content)
                        continue


    def read_log_tick_group(self, filename):
        types = {}
        for tg_tick, tg_time, tg_types, tg_content in read_log_raw_tick_group(filename):
            if 15 < len(tg_content):
                for logtype, content in tg_content:
                    types[logtype] = types.get(logtype,0) + 1
                for (search_type, search_strings), callbacks in self.searches.items():
                    if search_type in tg_types:
                        matched = [content for logtype, content in tg_content if logtype == search_type and all(ss in content for ss in search_strings)]
                        if matched:
                            for func_cb in callbacks:
                                func_cb(matched, tg_content)
                            continue

########################################
def read_log_raw_tick_group(filename):
    prior_log_tick = 0
    prior_log_time = 0
    tick_group = []
    tick_group_types = set()
    with open(filename, encoding='utf-8') as fi:
        for line in fi:
            if not line.startswith('['):
                continue
            log_type = line[30:].split(':')[0]
            log_tick = int(line[26:29])
            log_time = line[1:20] # ignore the three sub-second digits
            log_time = time.strptime(line[1:20], '%Y.%m.%d-%H.%M.%S')
            content = line[32+len(log_type):].rstrip('? ')
            if prior_log_tick != log_tick:
                if tick_group:
                    yield prior_log_tick, prior_log_time, tick_group_types, tick_group
                tick_group = []
                prior_log_tick = log_tick
                prior_log_time = log_time
            tick_group.append((log_type, content))
            tick_group_types.add(log_type)
        yield prior_log_tick, prior_log_time, tick_group_types, tick_group


################################################################################
if __name__ == '__main__':
    main()
