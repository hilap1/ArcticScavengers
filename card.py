import scoutCard
import refugeeCard
import hunterCard
import brawlerCard
import groupLeadersCard
import scavengerCard
import saboteurCard
import engineerCard
import sniperTeamCard
import thugsCard
import medicCard
import junkCard
import multitoolCard
import pickaxeCard
import rifleCard
import toolkitCard
import spearCard
import shovelCard
import netCard
import medkitCard
import pillsCard


class Card:

  def factory(self, name):
    builders = {
      "Scout": scoutCard.ScoutCard,
      "Refugee": refugeeCard.RefugeeCard,
      "Hunter": hunterCard.HunterCard,
      "Brawler": brawlerCard.BrawlerCard,
      "Group Leaders": groupLeadersCard.GroupLeadersCard,
      "Scavenger": scavengerCard.ScavengerCard,
      "Saboteur": saboteurCard.SaboteurCard,
      "Engineer": engineerCard.EngineerCard,
      "Sniper Team": sniperTeamCard.SniperTeamCard,
      "Thugs": thugsCard.ThugsCard,
      "Medic": medicCard.MedicCard,
      "Junk": junkCard.JunkCard,
      "Multitool": multitoolCard.MultitoolCard,
      "Pickaxe": pickaxeCard.PickaxeCard,
      "Rifle": rifleCard.RifleCard,
      "Toolkit": toolkitCard.ToolkitCard,
      "Spear": spearCard.SpearCard,
      "Shovel": shovelCard.ShovelCard,
      "Net": netCard.NetCard,
      "Medkit": medkitCard.MedkitCard,
      "Pills": pillsCard.PillsCard

    }
    return builders[name]()