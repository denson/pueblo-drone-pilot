<!-- Sanitized public copy: the prospective host business, its owner, its address,
coordinates, and the identifying links (facility website, county property records,
the nearby private airport's identifier) are deliberately withheld until the owner
agrees to be named. The unredacted original is held privately; the airspace analysis
publishes in full when the site is named. -->

# Low-Altitude Distributed Drone Pilot at the Prospective Host Facility

## A practical Part 107 pilot that can start before any BVLOS waiver

**Working date:** August 23, 2026  
**Pilot site:** a well-secured storage facility in Pueblo West, Colorado (name and exact location withheld until its owner agrees to be named)  
**Status:** Concept and regulatory planning document; not legal advice or an FAA authorization.

---

## 1. Executive conclusion

The simplest first version of the the facility drone project does **not** need to wait for a beyond-visual-line-of-sight (BVLOS) waiver.

the facility can host a relatively inexpensive, capable drone that is normally kept charged and ready. When a properly qualified person is physically present and can maintain visual line of sight (VLOS) with the aircraft throughout the flight, that person can operate the drone under ordinary Part 107 rules. The flight can still be highly automated: the operator can initiate a pre-programmed patrol, let the aircraft fly waypoints, point its camera at predefined locations, and command hold, return-to-base, land, or manual intervention as needed.

For this site, the routine patrol does not need to fly high. A practical design target is roughly **10-25 feet above the highest roofline or obstacle that the route must clear**, which will likely put much of the patrol in roughly the 30-50-foot-AGL range after a proper site survey. Part 107 sets a maximum altitude, but it does not require a drone to cruise hundreds of feet above the ground. Keeping the aircraft down in the built environment makes the mission easier to observe, reduces aviation exposure, improves useful camera geometry for a storage facility, and makes the public-facing concept easier to explain.

The regulatory dividing line is not whether the drone flies automatically. The key dividing line is **whether an authorized flight crew member can maintain the visual contact required by 14 CFR 107.31**. If the owner or a trained employee is on site and qualified, the drone can launch. If no qualified facility employee is present but a Part 107-certified deputy, firefighter, emergency-management responder, or other authorized pilot arrives, that responder can assume the pilot role and launch the same aircraft. If nobody is physically present and a county EOC or Sheriff's Office pilot wants to launch and operate the aircraft remotely, that is when BVLOS authority becomes necessary.

This produces a useful three-stage operating model:

1. **Facility VLOS mode:** a qualified the facility person is present and flies the facility patrol.
2. **Responder VLOS mode:** a qualified public-safety responder arrives, assumes responsibility for the aircraft, and flies it while maintaining VLOS.
3. **Future remote/BVLOS mode:** nobody needs to be physically present at the host site; an authorized remote public-safety pilot launches and supervises the drone under a valid BVLOS waiver or other appropriate FAA authority.

The important strategic change is that **BVLOS is no longer a prerequisite for proving the concept**. the facility can become a working demonstration site first, while the county decides whether a remote-launch capability is worth pursuing later.

---

## 2. The underlying idea: more modest drones, more widely distributed

The earlier concept centered on a large, expensive, long-endurance aircraft capable of traveling substantial distances across Pueblo County. That remains potentially useful for county-wide missions, but it is not the only architecture.

A second model is to place **less expensive but highly capable drones at multiple secure host facilities**. Storage facilities are particularly attractive hosts because they already tend to have fenced property, controlled access, electricity, internet service, cameras, open areas, and owners with a direct interest in security.

Instead of one long-range aircraft flying many miles to reach an incident, the county or another responder could use the **nearest pre-positioned aircraft**. A responder can also carry a small drone in a patrol car, but a hosted drone still has advantages when it is larger, has a better thermal/zoom payload, is kept charged, has a known launch area, and is already integrated with site networking and cameras.

The hosted-aircraft model therefore does not replace vehicle-carried drones. It creates another layer:

- small drones carried by individual responders;
- somewhat more capable drones pre-positioned at cooperative facilities; and
- potentially one or more long-endurance county aircraft for missions that genuinely need range and endurance.

The the facility pilot is a way to test the middle layer cheaply.

---

## 3. What ordinary Part 107 already allows

### 3.1 A qualified person can fly for business or public-safety purposes

The FAA's current Part 107 summary states that a person operating the controls under Part 107 must hold a Remote Pilot Certificate with a small-UAS rating **or be under the direct supervision of a certificated remote pilot who can immediately take control**. For routine independent operation at the facility, the cleaner model is to have the people expected to fly obtain their own Remote Pilot Certificates.

A Remote Pilot Certificate is an individual credential. It is not a special site permit. Once a person is current and is operating a properly registered aircraft in compliance with Part 107 and any applicable airspace requirements, that person can serve as the remote pilot in command (RPIC).

FAA recurrent training is required within the previous 24 calendar months for a certificated remote pilot to exercise Part 107 privileges. The recurrent online course is free.

### 3.2 VLOS is the central constraint

14 CFR 107.31 requires the flight crew to be able to see the aircraft throughout the flight with unaided vision other than corrective lenses so that they can know its location, determine its attitude and direction, observe the airspace, and make sure it is not endangering people or property.

That means it is not enough for a responder to be able to see the **storage facility**. The required crew member must be able to see the **drone itself throughout the flight**.

This matters for route design because rows of storage buildings can create blind spots. A route that disappears behind a building from the pilot's position can turn an otherwise simple VLOS operation into a problem. The pilot program should therefore be built around:

- a known pilot/observer position with broad visibility;
- patrol waypoints selected so the aircraft remains visible;
- route segments that do not hide behind buildings, signs, trees, or other structures; and
- optional use of a visual observer when that simplifies site coverage.

The route should be designed around VLOS from the beginning rather than trying to retrofit VLOS after the aircraft and software are selected.

### 3.3 A low patrol altitude is permissible

14 CFR 107.51 establishes a normal maximum altitude of 400 feet AGL, with a structure-related allowance above that in certain circumstances. It does not impose a general requirement that the drone fly high.

For the facility, the useful operational question is therefore not, "Can we fly at 100 feet?" but, "How low can we safely fly while clearing the actual buildings, lights, wires, signs, vehicles, poles, and other obstacles?"

A sensible starting design target is:

- approximately 10-25 feet of vertical clearance above the highest obstacle relevant to a particular route segment;
- a normal site ceiling substantially below 100 feet AGL;
- a hard software altitude limit above the planned patrol altitude but still low enough to keep the aircraft in the facility environment; and
- a separate emergency climb limit only if the selected autopilot requires one for obstacle avoidance or return-to-home behavior.

The exact altitude should be set only after measuring the site. "Roof plus 10 feet" is a useful concept, but the final route needs margin for rooftop equipment, poles, wires, GPS/altitude error, wind, and obstacle-avoidance behavior.

### 3.4 Automation does not by itself create a waiver requirement

The FAA's own operational guidance recognizes multiple levels of automation, including operator-initiated pre-programmed missions where the operator can regain control or can issue predefined commands such as land or return-to-base.

The Part 107 waiver page states the basic rule plainly: **if the operation complies with all Part 107 regulations, a waiver is not required**. Therefore, an operator-initiated waypoint patrol is not automatically a BVLOS operation just because the aircraft handles takeoff, waypoint navigation, camera pointing, return, or landing automatically.

For the the facility pilot, the preferred automation profile is:

1. Human checks the site, weather, aircraft status, and airspace.
2. Human initiates the patrol.
3. Aircraft automatically launches and follows a predefined route.
4. Human maintains required VLOS and watches the surrounding airspace.
5. Human can command hold, return, land, or manual intervention.
6. Aircraft returns to the designated landing area.
7. Flight is logged automatically.

That gives most of the convenience of autonomy without making autonomous decision-making the regulatory centerpiece.

---

## 4. the facility site and current airspace picture

### 4.1 Site identification

The facility's own website and county property records identify the site and list the property as approximately **4.5 acres**. (Identifying links are withheld along with the name.)

A public business-location listing is consistent with the location supplied for this project. (Coordinates withheld.)

### 4.2 Pueblo Memorial controlled airspace is well east of the site

The FAA identifies Pueblo Memorial Airport (PUB/KPUB) as a Class D airport. The published Pueblo Class D surface area is centered on Pueblo Memorial and extends only a few nautical miles around that airport. The facility is approximately **11 nautical miles from Pueblo Memorial Airport**, well outside that surface controlled-airspace radius.

Accordingly, the facility is in **uncontrolled Class G airspace at the surface under the current published airspace configuration**. Ordinary Part 107 operations in Class G do not require ATC permission or LAANC merely because they are drone operations.

This should still be rechecked before actual flights using current FAA-supported airspace tools because temporary restrictions, NOTAMs, and airspace changes can occur.

### 4.3 A small private airport is nearby, but it is not a towered controlled-airspace airport

A small private-use, non-towered airport with two dirt runways lies approximately **two nautical miles from the facility**. (The airport identifier is withheld with the site identity; FAA-derived data confirms its class.)

The FAA's guidance for airports in uncontrolled airspace says that prior airspace authorization is not required for drone flights below 400 feet AGL merely because they are near such an airport. The drone operator must, however:

- avoid airport traffic patterns and takeoff/landing areas;
- not interfere with airport operations; and
- yield right of way to every crewed aircraft.

For a the facility patrol conducted roughly 30-50 feet AGL, ordinary fixed-wing airport traffic should normally be far above the drone. That does not eliminate the RPIC's duty to watch for unusual low-level traffic, helicopters, emergency aircraft, agricultural aircraft, or abnormal operations. A simple site rule should be: **if any crewed aircraft appears to present a possible conflict, descend/land immediately and yield.**

### 4.4 LAANC is not expected to be part of routine the facility flights

The FAA requires airspace authorization in Class B, C, D, and surface Class E controlled airspace. The FAA also makes clear that UAS Facility Maps are informational tools for processing controlled-airspace authorization requests; they do not themselves authorize flight.

Because the facility is outside Pueblo Memorial's surface controlled airspace and the nearby private airport does not create its own controlled surface area, routine low-altitude Part 107 operations at the site should not require LAANC under the current airspace configuration.

The preflight process should nevertheless include an airspace/restrictions check every time.

---

## 5. Night operations

Night operation is important because storage-facility incidents may occur after office hours.

Current Part 107 rules allow routine night operations without a special night waiver when the applicable requirements are met. The RPIC must have completed the appropriate current initial or recurrent training, and the drone must use anti-collision lighting visible for at least three statute miles with a sufficient flash rate.

Therefore, the the facility pilot can be designed for night operation from the beginning. The system should include:

- compliant anti-collision lighting;
- thermal imaging if budget permits;
- fixed site lighting that does not blind the drone camera or pilot;
- a clearly visible landing zone;
- route lighting/obstacle documentation; and
- separate day and night operating limits if necessary.

A low nighttime route also makes VLOS engineering important: the pilot must be able to identify and continuously see the aircraft, not merely its camera feed.

---

## 6. People, vehicles, and a storage-facility environment

A storage facility is not empty airspace. Customers may be walking between units, driving trucks or trailers, or loading property. Part 107 has specific rules for operations over people and moving vehicles.

The easiest initial pilot design is to avoid making those rules the center of the project:

- keep the routine route over roofs, perimeter lanes, setbacks, or other areas that minimize overflight of uninvolved people;
- do not intentionally hover or maintain sustained flight over customers or moving vehicles unless the selected aircraft and operation meet the applicable rule;
- use fixed cameras and site procedures to check the launch/recovery area before takeoff and landing; and
- if necessary, pause the patrol until a person or vehicle clears a route segment.

Because the facility is gated and access-controlled, it may be possible to establish notice and restricted-access procedures that help with some operations, but the first pilot should use conservative route design rather than depend on complicated Operations Over People classifications.

---

## 7. Aircraft registration, Remote ID, and basic compliance

The first aircraft should be treated as an ordinary Part 107 aircraft unless the county later chooses a public-aircraft operating path.

Basic Part 107 setup includes:

- FAA registration;
- required aircraft marking;
- Remote ID compliance for an aircraft that requires registration, unless a specific exception applies;
- preflight inspection and aircraft-condition checks;
- confirmation of command/control link status;
- current pilot credential and recurrent training;
- current airspace/restrictions review; and
- basic flight records and incident reporting procedures.

These are ordinary compliance tasks, not a special permit package for the facility.

---

## 8. Who can fly the the facility aircraft

### Mode A - the owner or a facility employee

If the owner or another employee obtains and maintains a Part 107 Remote Pilot Certificate, that person can serve as RPIC for routine VLOS facility patrols.

This is the simplest private-facility use case:

**alarm or concern -> qualified employee checks conditions -> employee launches patrol -> aircraft follows predefined route -> employee maintains VLOS and can intervene -> aircraft returns and lands.**

No BVLOS waiver is needed because the flight remains VLOS.

### Mode B - Employee manipulating controls under direct supervision

Part 107 also allows a non-certificated person to manipulate the flight controls when directly supervised by a certificated RPIC who can immediately take direct control.

This can be useful for training, but it is not the preferred long-term operating model for a facility expected to respond independently. Independent regular operators should simply earn the Part 107 certificate.

### Mode C - A certified responder arrives and uses the pre-positioned aircraft

A sheriff's deputy, firefighter, emergency-management responder, search-and-rescue member, or other authorized responder who holds a current Part 107 certificate could potentially operate the aircraft once on scene, subject to agency policy, owner authorization, insurance, aircraft-account procedures, and any applicable interagency agreement.

The responder does not need to have carried that particular drone in the vehicle. The practical requirement is that the responder lawfully assumes the RPIC role and can maintain VLOS with the aircraft throughout the operation.

This is one of the strongest arguments for pre-positioning aircraft. The responder can arrive at a known site where the drone is already charged, connected, and ready rather than transporting, unpacking, charging, and configuring a larger aircraft on every call.

### Mode D - Remote EOC/Sheriff operation with nobody on site

This is the future upgrade.

If an EOC or Sheriff's Office pilot launches and operates the aircraft while nobody at the facility can provide the required VLOS, the operation is BVLOS. Under current Part 107 rules, that requires appropriate FAA authority, such as a Section 107.31 waiver, unless another valid public-aircraft authorization applies.

This is where the Pueblo Police Department's existing BVLOS experience becomes a useful local model. The FAA's public waiver list shows a Pueblo Police Department waiver issued August 4, 2026 covering Sections 107.31, 107.39, and 107.145. That City waiver is not transferable to Pueblo County, but it proves that the FAA is currently issuing this type of authority to local public-safety organizations.

The county does not need that authority to start the the facility VLOS pilot.

---

## 9. Proposed low-altitude patrol design

The first route should be deliberately boring and repeatable.

### Normal flight envelope

**Horizontal:** facility property or a slightly smaller internal geofence.  
**Vertical:** just high enough to clear the measured site obstacles, likely far below 100 feet AGL.  
**Speed:** slow enough for useful video and easy visual tracking.  
**Launch/recovery:** one marked area with clear approach and departure paths.  
**Mission:** inspection/patrol, not pursuit outside the geofence.

### Example sequence

1. RPIC receives an alarm or decides to perform a patrol.
2. RPIC checks current weather, restrictions, aircraft status, and the launch area.
3. RPIC confirms no person/vehicle is in the immediate launch path.
4. RPIC selects **Facility Patrol**.
5. Drone launches to a low safe transit height.
6. Drone follows a predefined path along visible portions of the facility perimeter and storage rows.
7. Camera automatically looks at gates, fence lines, vehicle-storage areas, roofs, or other predefined points.
8. RPIC maintains visual contact and monitors the surrounding airspace.
9. RPIC can command **HOLD**, **LAND**, **RETURN**, or manual control.
10. Drone returns to the marked landing area and shuts down.
11. Software logs the mission and saves video according to the facility's policy.

### Software safety features worth requiring

- horizontal geofence;
- low altitude ceiling;
- predefined return-to-home altitude appropriate for the actual obstacles;
- lost-link behavior tested at the site;
- low-battery automatic return/landing;
- manual abort/land control;
- weather/wind limit warnings;
- route version control so an accidental waypoint change cannot send the aircraft off site; and
- automatic flight logging.

---

## 10. Why the site-hosted aircraft can still be useful when responders carry drones

It is reasonable to ask why a sheriff's deputy would use a storage-facility drone if a small drone can simply ride in the patrol vehicle.

The hosted drone earns its place if it offers one or more of these advantages:

- larger thermal/zoom payload than practical for every patrol car;
- always charged and ready;
- protected from vehicle heat/cold and daily handling;
- no unpacking or assembly;
- known launch and landing area;
- known obstacle map and geofence;
- fixed internet connection and backup communications;
- integration with facility alarms and cameras;
- shared access by multiple public-safety organizations; and
- later conversion to remote BVLOS operation without moving the base site.

Therefore, the hosted drone should not merely duplicate the cheapest drone already carried by deputies. It should occupy the useful middle ground between a pocket/patrol-car aircraft and a very expensive long-endurance county platform.

---

## 11. Why the facility is a good first demonstration site

the facility has several characteristics that fit this concept:

- locally owned and therefore potentially able to make decisions quickly;
- gated, controlled-access property;
- 24/7 tenant access, creating a genuine after-hours security use case;
- existing video surveillance/security orientation;
- drive-up layout and open lanes that can support a low patrol route;
- electricity and internet availability;
- approximately 4.48 acres, large enough to demonstrate useful patrol behavior but small enough to keep the flight tightly bounded;
- Class G airspace at the surface under the current published configuration; and
- proximity to Pueblo West public-safety operations without being inside Pueblo Memorial's controlled surface airspace.

The site is also useful politically because the first aircraft can begin as a **private-facility Part 107 pilot** rather than a permanently airborne police-surveillance system. Public-safety use can be demonstrated incrementally.

---

## 12. Relationship to Pueblo County S.O.A.R.R.

Pueblo County Sheriff's Office already has an established UAS capability. Its 2024 accountability report says the Sheriff's Office Aerial Response & Rescue (S.O.A.R.R.) Team operated a fleet of 13 UAVs, responded to 32 callouts, completed 110 flights, and logged more than 14 flight hours supporting crime-scene work, crashes, events, missing-person searches, and urgent operations.

That matters because the county is not being asked to learn what a drone is or create an aviation program from zero.

The the facility pitch can be narrower:

> **Pre-position one compatible aircraft at a secure Pueblo West host site. Let the host's trained pilots use it for lawful VLOS facility patrols. Let qualified county responders use it on scene when appropriate. If the concept proves useful, later pursue the authority needed for remote launch from the EOC/Sheriff's Office when nobody is physically present.**

This is an extension of an existing local capability, not a replacement for S.O.A.R.R.

---

## 13. What requires no special waiver, and what does

| Operation | Special BVLOS waiver needed? | Notes |
|---|---:|---|
| Qualified the facility pilot flies while maintaining VLOS | **No** | Ordinary Part 107 requirements still apply. |
| Operator starts an automated waypoint patrol but maintains VLOS and can intervene/command safe actions | **No, solely because of automation** | Flight still must comply with all Part 107 rules. |
| Routine patrol at roughly roof height plus safe clearance | **No** | Must remain within normal Part 107 limitations and safe obstacle margins. |
| Night patrol with current Part 107 training and compliant anti-collision lighting | **No night waiver** | Other Part 107 rules still apply. |
| Certified responder arrives and flies the hosted drone while maintaining VLOS | **No BVLOS waiver** | Subject to ownership, agency policy, insurance, and operational control arrangements. |
| Flight in Class G at the facility under current airspace configuration | **No ATC/LAANC authorization** | Must recheck current restrictions before flight. |
| EOC/Sheriff pilot launches remotely while nobody can maintain required VLOS | **Yes, under current Part 107** | Requires Section 107.31 waiver or other appropriate authority. |
| Drone leaves the visual operating area to chase/follow a subject beyond VLOS | **Yes, under current Part 107** | The geofence should prevent this in the initial pilot. |

---

## 14. Recommended first pilot scope

The first pilot should be deliberately modest.

### Phase 1 - Site engineering

- obtain an accurate property map;
- measure rooflines, poles, wires, lights, signs, trees, and other obstacles;
- identify the best pilot observation position;
- define one launch/recovery area;
- design a route that stays in continuous VLOS;
- define a low geofence and altitude ceiling;
- document the nearby private airport and expected traffic direction; and
- test cell/internet/Wi-Fi/radio coverage if the aircraft uses network services.

### Phase 2 - Aircraft and software selection

Select a drone based on the facility mission rather than county-wide range. Priorities should include:

- thermal camera if financially practical;
- useful optical zoom;
- good low-light performance;
- stable automated waypoint flight;
- reliable geofencing;
- return/land controls;
- wind tolerance appropriate to Pueblo West;
- Remote ID compliance;
- simple battery logistics;
- secure user accounts; and
- ability to export flight logs and video.

### Phase 3 - Train facility pilots

Train at least two people rather than one so the operation is not dependent on a single individual. Each regular independent pilot should obtain a Part 107 Remote Pilot Certificate and complete site-specific training.

Site-specific training should cover:

- the approved route;
- VLOS positions and blind spots;
- launch/landing checks;
- nearby-aircraft response;
- night operations;
- wind and weather limits;
- customer/vehicle separation;
- lost-link and low-battery procedures;
- manual landing and emergency stop; and
- incident/video handling.

### Phase 4 - Build a flight-history record

Conduct repeated low-risk VLOS patrols and record:

- takeoff and landing success;
- route completion;
- battery consumption;
- wind conditions;
- GPS/position performance;
- video usefulness;
- lost-link tests;
- abort/return tests;
- human/vehicle conflicts; and
- maintenance events.

This creates evidence for both the business case and any later BVLOS application.

### Phase 5 - Invite county/fire/emergency-management participation

Once the system is demonstrably safe and useful, invite qualified local public-safety personnel to observe or participate in controlled demonstrations. The question becomes concrete: **Would having this aircraft already sitting here improve your response capability?**

### Phase 6 - Decide whether BVLOS is worth pursuing

Only after the VLOS pilot shows value should the project invest serious time in remote-launch authority. If the answer is yes, Pueblo Police Department's current waiver and other Colorado public-safety BVLOS waivers can be used as models for the county's application.

---

## 15. Key operational rules for the first the facility version

A concise initial rule set could be:

1. **No flight without a designated RPIC.**
2. **RPIC or authorized visual observer maintains required VLOS throughout the flight.**
3. **Routine patrol remains inside the facility geofence.**
4. **Routine altitude stays only as high as necessary for safe obstacle clearance; target substantially below 100 feet AGL.**
5. **Yield immediately to any crewed aircraft; descend or land if there is any possible conflict.**
6. **Do not fly intentionally over uninvolved people or moving vehicles unless the operation is specifically compliant with the applicable rule.**
7. **Night flights require current training and compliant anti-collision lighting.**
8. **Preflight includes weather, airspace/restrictions, aircraft health, launch area, and link checks.**
9. **Lost-link, low-battery, and return-to-home behavior must be tested at the actual site.**
10. **No pursuit outside the approved facility route during the initial pilot.**
11. **Every flight is logged.**
12. **Remote launch with nobody able to maintain VLOS is not allowed until appropriate FAA authority is obtained.**

---

## 16. Open questions before buying anything

The concept is straightforward enough that the next work should focus on engineering details rather than broad regulatory research.

The main unresolved questions are:

- exact property boundary and usable launch area;
- actual roof/obstacle heights;
- best VLOS observation point;
- whether one observer position can see the entire desired route;
- desired thermal and optical camera capability;
- desired flight time;
- wind requirement;
- whether the drone will be stored inside a unit, weather enclosure, or simple dock;
- how quickly a human can deploy it;
- whether the owner wants staff trained as independent Part 107 pilots;
- whether the Sheriff's Office, Pueblo West Fire, or other responders would be willing to operate a privately hosted aircraft;
- ownership, insurance, indemnification, and access-control arrangements for responder use; and
- what level of integration, if any, should exist between facility alarms and drone mission software.

The aircraft should be chosen **after** those questions are answered.

---

## 17. Bottom line

The first the facility drone does not have to be a six-figure aircraft and does not have to wait for the county to obtain BVLOS authority.

A practical first system is a relatively inexpensive, thermal-capable or upgradeable drone stored at the facility, configured with a very low geofenced patrol route, and operated under ordinary Part 107 whenever a qualified person is physically present and can keep the aircraft in visual line of sight.

That person can be a trained the facility employee. It can also be an authorized Part 107-certified public-safety responder who arrives at the property and lawfully assumes control of the aircraft. The drone can fly an automated patrol while the human remains responsible for the operation and can command it to hold, return, land, or otherwise respond to hazards.

The more ambitious remote-EOC model remains available later. But it should be treated as **Phase 2**, not as the condition that determines whether Phase 1 can exist.

The resulting strategy is simple:

> **Build something useful under ordinary Part 107 first. Prove that a low, geofenced, pre-positioned drone at the facility adds value. Then decide whether removing the on-site VLOS requirement is worth the additional FAA work.**

---

## 18. Primary sources and reference links

### FAA / federal rules

1. FAA - Small Unmanned Aircraft Systems Regulations (Part 107):  
   https://www.faa.gov/newsroom/small-unmanned-aircraft-systems-uas-regulations-part-107

2. eCFR - 14 CFR 107.31, Visual line of sight aircraft operation:  
   https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-B/section-107.31

3. eCFR - 14 CFR 107.51, Operating limitations for small unmanned aircraft:  
   https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-B/section-107.51

4. eCFR - 14 CFR 107.29, Operation at night:  
   https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-B/section-107.29

5. eCFR - 14 CFR 107.37, Operation near aircraft; right-of-way rules:  
   https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-107/subpart-B/section-107.37

6. FAA - Become a Certificated Remote Pilot:  
   https://www.faa.gov/uas/commercial_operators/become_a_drone_pilot

7. FAA - Remote Identification of Drones:  
   https://www.faa.gov/uas/getting_started/remote_id

8. FAA - Flying Near Airports:  
   https://www.faa.gov/uas/getting_started/where_can_i_fly/airspace_restrictions/flying_near_airports

9. FAA - UAS Facility Maps:  
   https://www.faa.gov/uas/commercial_operators/uas_facility_maps

10. FAA - Part 107 Airspace Authorizations / LAANC:  
    https://www.faa.gov/uas/commercial_operators/part_107_airspace_authorizations

11. FAA - Part 107 Waivers:  
    https://www.faa.gov/uas/commercial_operators/part_107_waivers

12. FAA - Instructions describing levels of UAS automation and geofencing:  
    https://www.faa.gov/uas/advanced_operations/instructions-drone-operators-completing-faa-form-7711-2

13. FAA - Operations Over People and Moving Vehicles:  
    https://www.faa.gov/uas/commercial_operators/operations_over_people

14. FAA - Pueblo Memorial Airport information (identifies PUB as Class D):  
    https://www.faa.gov/flight_deck/pub

15. FAA - Issued Part 107 waivers, including Pueblo Police Department's August 4, 2026 waiver:  
    https://www.faa.gov/uas/commercial_operators/part_107_waivers/waivers_issued

### Site and local sources

16. The facility's official site: withheld with the name

17. The facility's contact/location page: withheld with the name

18. Pueblo County property notice for the facility: withheld with the name

19. Pueblo Regional Building Department commercial building record: withheld with the name

20. FAA-derived data for the nearby private airport via AirNav: withheld with the site identity

21. FAA-derived data for the nearby private airport via SkyVector: withheld with the site identity

22. Pueblo County Sheriff's Office - 2024 Accountability Report (S.O.A.R.R. activity):  
    https://www.pueblosheriff.com/Archive.aspx?ADID=5493

### Planning note

This report reflects publicly available rules and records checked on August 23, 2026. Airspace status, temporary flight restrictions, NOTAMs, aircraft software behavior, and agency policies must be rechecked before actual operations. Nothing in this report substitutes for the RPIC's legal responsibilities or for advice from the FAA, agency counsel, or an aviation attorney where appropriate.
