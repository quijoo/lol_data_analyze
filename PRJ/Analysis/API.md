## Match

* `/lol/match/v4/matches/{matchId}`

  ```python
  header = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
      "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
      "Origin": "https://developer.riotgames.com",
      "X-Riot-Token": token
  }
  ```

  

  ```python
  	input = matchId
  	output  = {
          gameId	long,
          queueId			int,
          gameType 		str,
          gameDuration 	long, #比赛持续时间,
          platformId		string,
          gameCreation	long(时间戳),
          seasonId		int,
          gameVersion		string,
          mapId			int,
          gameMode		string,
          
          participantIdentities	List[participantIdentityDto]{
              player	List[playerDto]{
                  profileIcon			int	
  				accountId			string	# 玩家原始加密id
  				matchHistoryUri		string	
  				currentAccountId	string	# 玩家当前加密ID
  				currentPlatformId	string	
  				summonerName		string	# 玩家昵称
  				summonerId			string	# 加密玩家昵称
  				platformId			string	# 原始平台id			
              }
          },
          
          
          team	List[TeamStatDto]{
                      towerKills		int 				# 当前队伍推塔数量
                      riftHeraldKills	int					# 击杀的峡谷先锋数量
                      firstBlood		boolean				# 是否取得一血
                      inhibitorKills	int					# 摧毁的召唤水晶数量.
                      firstBaron				boolean	
                      firstDragon				boolean		# 大龙一血
                      dominionVictoryScore	int			# 比赛结束时的得分
                      dragonKills				int			# 击杀Dragon的次数.
                      baronKills				int			# 击杀Baron的次数.
                      firstInhibitor			boolean		# 是否摧毁第一个召唤水晶
                      firstTower				boolean		# 是都摧毁的一个塔
                      vilemawKills			int			# 击杀 Vilemaw的次数.
                      firstRiftHerald			boolean		# 是否击杀第一个裂谷先锋
                      teamId					int			# 100：blue， 200：red
                      win						string		# 团队是否获胜 (Legal values: Fail, Win)
                      bans	List[TeamBansDto]{
                          championId	int	# 被ban掉的英雄ID.
                          pickTurn	int	# 被ban的优先级
                      }
          	},
          
          participants List[ParticipantDto]{
              participantId	int	
              championId		int
              teamId	int							# 100 for blue side. 200 for red side
              spell1Id	int						# 第一召唤者法术ID
              spell2Id	int						# 第二召唤者法术ID
              highestAchievedSeasonTier	string	# 段位
              timeline	ParticipantTimelineDto 	# 下表单独列出时间轴信息
              stats		ParticipantStatsDto		# 下表单独列出
              runes		List[RuneDto]{			# 符文信息列表
               				runeId	int	
  							rank	int  	# 等级
              			}
              masteries	List[MasteryDto]{		# 英雄掌握？信息列表。不包括与符文重新合并的比赛？？？
                  rank	int	
  				masteryId	int
              }	
              
          }
      }
  ```

  

  

  ```python
  ParticipantTimelineDto {
          participantId	int	
          csDiffPerMinDeltas	Map[String, double]
      	# Creep score difference versus the calculated lane opponent(s) for a specified period.
          
      	damageTakenPerMinDeltas	Map[String, double]
      	# Damage taken for a specified period.
          
      	role	string	# 
      	# Participant's calculated role. (Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT)
          
      	damageTakenDiffPerMinDeltas	Map[String, double]
      	# Damage taken difference versus the calculated lane opponent(s) for a specified period.
          
      
      	xpPerMinDeltas	Map[String, double]
      	# Experience change for a specified period.
          
      
      	xpDiffPerMinDeltas	Map[String, double]	
      	# Experience difference versus the calculated lane opponent(s) for a specified period.
          
      	lane	string	
      	# Participant's calculated lane. MID and BOT are legacy values. 
      	# (Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM)
          
      	creepsPerMinDeltas	Map[String, double]	# Creeps for a specified period.
          goldPerMinDeltas	Map[String, double]	# Gold for a specified period.
  }
  ```

  ```python
  ParticipantTimelineDto{
  	item0	int	
      item2	int	
      totalUnitsHealed	int	
      item1	int	
      largestMultiKill	int	
      goldEarned	int	
      firstInhibitorKill	boolean	
      physicalDamageTaken	long	
      nodeNeutralizeAssist	int	
      totalPlayerScore	int	
      champLevel	int	
      damageDealtToObjectives	long	
      totalDamageTaken	long	
      neutralMinionsKilled	int	
      deaths	int	
      tripleKills	int	
      magicDamageDealtToChampions	long	
      wardsKilled	int	
      pentaKills	int	
      damageSelfMitigated	long	
      largestCriticalStrike	int	
      nodeNeutralize	int	
      totalTimeCrowdControlDealt	int	
      firstTowerKill	boolean	
      magicDamageDealt	long	
      totalScoreRank	int	
      nodeCapture	int	
      wardsPlaced	int	
      totalDamageDealt	long	
      timeCCingOthers	long	
      magicalDamageTaken	long	
      largestKillingSpree	int	
      totalDamageDealtToChampions	long	
      physicalDamageDealtToChampions	long	
      neutralMinionsKilledTeamJungle	int	
      totalMinionsKilled	int	
      firstInhibitorAssist	boolean	
      visionWardsBoughtInGame	int	
      objectivePlayerScore	int	
      kills	int	
      firstTowerAssist	boolean	
      combatPlayerScore	int	
      inhibitorKills	int	
      turretKills	int	
      participantId	int	
      trueDamageTaken	long	
      firstBloodAssist	boolean	
      nodeCaptureAssist	int	
      assists	int	
      teamObjective	int	
      altarsNeutralized	int	
      goldSpent	int	
      damageDealtToTurrets	long	
      altarsCaptured	int	
      win	boolean	
      totalHeal	long	
      unrealKills	int	
      visionScore	long	
      physicalDamageDealt	long	
      firstBloodKill	boolean	
      longestTimeSpentLiving	int	
      killingSprees	int	
      sightWardsBoughtInGame	int	
      trueDamageDealtToChampions	long	
      neutralMinionsKilledEnemyJungle	int	
      doubleKills	int	
      trueDamageDealt	long	
      quadraKills	int	
      item4	int	
      item3	int	
      item6	int	
      item5	int	
      playerScore0	int	
      playerScore1	int	
      playerScore2	int	
      playerScore3	int	
      playerScore4	int	
      playerScore5	int	
      playerScore6	int	
      playerScore7	int	
      playerScore8	int	
      playerScore9	int	
      perk0	int	Primary path keystone rune.
      perk0Var1	int	Post game rune stats.
      perk0Var2	int	Post game rune stats.
      perk0Var3	int	Post game rune stats.
      perk1	int	Primary path rune.
      perk1Var1	int	Post game rune stats.
      perk1Var2	int	Post game rune stats.
      perk1Var3	int	Post game rune stats.
      perk2	int	Primary path rune.
      perk2Var1	int	Post game rune stats.
      perk2Var2	int	Post game rune stats.
      perk2Var3	int	Post game rune stats.
      perk3	int	Primary path rune.
      perk3Var1	int	Post game rune stats.
      perk3Var2	int	Post game rune stats.
      perk3Var3	int	Post game rune stats.
      perk4	int	Secondary path rune.
      perk4Var1	int	Post game rune stats.
      perk4Var2	int	Post game rune stats.
      perk4Var3	int	Post game rune stats.
      perk5	int	Secondary path rune.
      perk5Var1	int	Post game rune stats.
      perk5Var2	int	Post game rune stats.
      perk5Var3	int	Post game rune stats.
      perkPrimaryStyle	int	Primary rune path
      perkSubStyle	int	Secondary rune path    
  }
  
  ```

  





### Table1

| 字段名称       | 数据类型 | 数据长度 | 说明             | 主键 |
| -------------- | -------- | -------- | ---------------- | ---- |
| uid            | int      | 256      | 用户ID           | 是   |
| gid            | int      | 256      | 比赛ID           | 是   |
| cid            | string   | 256      | 英雄ID           | 否   |
| role           | string   | 256      | 角色             | 否   |
| lane           | String   | 256      | 线路             | 否   |
| win            | Int      | 20       | 是否获胜         | 否   |
| season         | Int      | 256      | 赛季             | 否   |
| rank           | String   | 256      | 段位             | 否   |
| totalkill      | Int      | 256      | 总击杀           | 否   |
| totalkilled    | Int      | 256      | 总被杀           | 否   |
| totalassist    | Int      | 256      | 总助攻           | 否   |
| versusid       | string   | 256      | 对位英雄ID       | 否   |
| tower          | Int      | 256      | 推塔数           | 否   |
| damagetaken    | long     | 512      | 承伤             | 否   |
| heal           | long     | 512      | 治疗             | 否   |
| killcounter    | Int      | 256      | 击杀对位英雄数   | 否   |
| killedcounter  | Int      | 256      | 被对位英雄击杀数 | 否   |
| firsttowertime | long     | 256      | 拿对位一塔时间   | 否   |
| csdiffer       | int      | 256      | 十分钟压刀数     | 否   |
| damage         | long     | 512      | 输出             | 否   |





### Table2

| 字段名称       | 数据类型 | 数据长度 | 说明   | 主键 |
| -------------- | -------- | -------- | ------ | ---- |
| cid            | string   | 256      | 英雄ID | 是   |
| rank           | int      | 256      | 段位   | 否   |
| version        | Int      | 256      | 版本   | 否   |
| appearancerate | Int      | 256      | 登场率 | 否   |
| winrate        | Int      | 256      | 总胜率 | 否   |

* 以 （cid，version, rank） 为 key
* 计算胜率 / 出场率



### Table3

| 字段名称           | 数据类型 | 数据长度 | 说明     | 主键 |
| ------------------ | -------- | -------- | -------- | ---- |
| cid                | string   | 256      | 英雄ID   | 是   |
| version            | int      | 256      | 版本     | 是   |
| averagekill        | Double   | 256      | 场均击杀 | 否   |
| (dele)averagetower | Double   | 256      | 场均推塔 | 否   |
| averagekilled      | Double   | 256      | 场均被杀 | 否   |
| averagedamage      | Long     | 512      | 场均伤害 | 否   |
| averagedamaged     | Long     | 512      | 场均承伤 | 否   |
| averageheal        | Long     | 512      | 场均治疗 | 否   |
| averageassist      | Double   | 256      | 场均助攻 | 否   |





### Table4

| 字段名称 | 数据类型 | 数据长度 | 说明             | 主键 |
| -------- | -------- | -------- | ---------------- | ---- |
| cid      | String   | 256      | 英雄ID           | 是   |
| version  | int      | 256      | 版本             | 是   |
| role     | string   | 256      | 角色             | 否   |
| lane     | String   | 256      | 线路             | 否   |
| versusid | string   | 256      | 对英雄ID         | 否   |
| cwinrate | Int      | 20       | 对位胜率         | 否   |
| kdr      | Int      | 256      | 战损比           | 否   |
| kda      | String   | 256      | KDA              | 否   |
| csdiffer | Int      | 256      | 场均十分钟压刀数 | 否   |



### Table_zrh

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

