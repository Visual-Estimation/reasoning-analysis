# ANGLE Estimation: Worst 30 Cases Reasoning Analysis

Worst 10 per batch for each model (OpenAI, Gemini, Gemini-Robotics), ranked by |log₁₀(pred/GT)|

---

# OPENAI MODEL

## BATCH 1

### #1: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 170.0
- Ratio (Pred/GT): 22.08× (OVER)
- Error: 2107.8%

**Reasoning Trace:**
> The pedal top is nearly horizontal, and the connected arm on the right slopes only slightly downward, so the marked interior angle is close to a straight line at about 170°.

---

### #2: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 92.0
- Ratio (Pred/GT): 4.09× (OVER)
- Error: 308.9%

**Reasoning Trace:**
> The highlighted lower support appears to meet the slanted main panel at დაახლოებით a right angle, so the marked bend is close to 90 degrees.

---

### #3: `M-angle-image3.jpg`

**Prediction Metrics:**
- Ground Truth: 18.85
- Prediction: 64.0
- Ratio (Pred/GT): 3.40× (OVER)
- Error: 239.5%

**Reasoning Trace:**
> The marked ray rises moderately steeply from the horizontal baseline, appearing to form an acute angle of roughly mid-60s degrees.

---

### #4: `M-angle-image12.jpg`

**Prediction Metrics:**
- Ground Truth: 22.0
- Prediction: 48.0
- Ratio (Pred/GT): 2.18× (OVER)
- Error: 118.2%

**Reasoning Trace:**
> The red mark points to the hanger’s left slanted side, which appears moderately steep relative to the horizontal seat/floor reference, at about the upper-40s in degrees.

---

### #5: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 100.0
- Ratio (Pred/GT): 2.08× (OVER)
- Error: 108.3%

**Reasoning Trace:**
> The long shaft is roughly 45° above horizontal, while the short lower piece is about 55° below horizontal, so the included bend angle is about 100°.

---

### #6: `V-angle-image59-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 95.0
- Ratio (Pred/GT): 2.02× (OVER)
- Error: 102.1%

**Reasoning Trace:**
> The marked corner is formed by two edges of the ottoman that appear nearly perpendicular, giving an angle close to a right angle.

---

### #7: `V-angle-image69.jpg`

**Prediction Metrics:**
- Ground Truth: 52.0
- Prediction: 102.0
- Ratio (Pred/GT): 1.96× (OVER)
- Error: 96.2%

**Reasoning Trace:**
> The red board appears tilted about 78° relative to the floor, and the marked arc is the obtuse outside angle on the left side, so it is about 180° - 78° ≈ 102°.

---

### #8: `V-angle-image66.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 123.0
- Ratio (Pred/GT): 1.86× (OVER)
- Error: 85.9%

**Reasoning Trace:**
> The red mark indicates the exterior angle at the lower corner between the slanted side member and the lower edge/its extension; visually it is a little over 120°.

---

### #9: `P-angle-image9.jpg`

**Prediction Metrics:**
- Ground Truth: 37.2
- Prediction: 65.0
- Ratio (Pred/GT): 1.75× (OVER)
- Error: 74.7%

**Reasoning Trace:**
> The leaning wooden plank appears to make an acute angle of roughly two-thirds of a right angle with the local ground line, about 65 degrees.

---

### #10: `V-angle-image41.jpg`

**Prediction Metrics:**
- Ground Truth: 70.9
- Prediction: 120.0
- Ratio (Pred/GT): 1.69× (OVER)
- Error: 69.3%

**Reasoning Trace:**
> The marked arc is the exterior angle at the lower-right joint between the slanted side bar and the lower bar, which appears a little obtuse—about 120 degrees.

---

## BATCH 2

### #1: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 80.0
- Ratio (Pred/GT): 3.56× (OVER)
- Error: 255.6%

**Reasoning Trace:**
> The lower wooden support appears to join the slanted main panel at a little less than a right angle, so the marked joint is about 80 degrees.

---

### #2: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 165.0
- Ratio (Pred/GT): 3.44× (OVER)
- Error: 243.8%

**Reasoning Trace:**
> The two connected parts at the marked lower joint appear almost straight with a slight bend, making the interior joint angle roughly in the mid-160s.

---

### #3: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 25.0
- Ratio (Pred/GT): 3.25× (OVER)
- Error: 224.7%

**Reasoning Trace:**
> The marked corner forms a small acute angle between the nearly horizontal top edge and the slanted adjoining part, which looks to be about a quarter of a right angle.

---

### #4: `M-angle-image3.jpg`

**Prediction Metrics:**
- Ground Truth: 18.85
- Prediction: 55.0
- Ratio (Pred/GT): 2.92× (OVER)
- Error: 191.8%

**Reasoning Trace:**
> The marked joint looks like a moderate acute bend; the two meeting parts appear to form an angle in the mid-50s.

---

### #5: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 60.0
- Ratio (Pred/GT): 2.12× (OVER)
- Error: 112.0%

**Reasoning Trace:**
> The marked contact is an acute angle between the slanted package edge and the floor, which looks to be about sixty degrees.

---

### #6: `V-angle-image73.jpg`

**Prediction Metrics:**
- Ground Truth: 47.6
- Prediction: 95.0
- Ratio (Pred/GT): 2.00× (OVER)
- Error: 99.6%

**Reasoning Trace:**
> The red mark is between the container’s left edge and the table’s left outer edge at the contact point; visually it looks close to a right angle, slightly obtuse.

---

### #7: `V-angle-image66.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 124.0
- Ratio (Pred/GT): 1.87× (OVER)
- Error: 87.5%

**Reasoning Trace:**
> The red mark indicates the exterior angle between the board’s side rail and the lower edge/its extension at the corner, which looks a little over 120 degrees.

---

### #8: `V-angle-image51.jpg`

**Prediction Metrics:**
- Ground Truth: 62.05
- Prediction: 115.0
- Ratio (Pred/GT): 1.85× (OVER)
- Error: 85.3%

**Reasoning Trace:**
> The marked angle appears to be the obtuse angle between the leaning book and the floor at the base; the book is about 65° to the horizontal, so the highlighted angle is about 180° - 65° = 115°.

---

### #9: `V-angle-image41.jpg`

**Prediction Metrics:**
- Ground Truth: 70.9
- Prediction: 125.0
- Ratio (Pred/GT): 1.76× (OVER)
- Error: 76.3%

**Reasoning Trace:**
> The highlighted mark appears to indicate the exterior angle between the slanted right leg and the bottom bar’s extension, which looks a bit larger than 120° in the image.

---

### #10: `P-angle-image9.jpg`

**Prediction Metrics:**
- Ground Truth: 37.2
- Prediction: 65.0
- Ratio (Pred/GT): 1.75× (OVER)
- Error: 74.7%

**Reasoning Trace:**
> The leaning wood plank appears to be about 25° away from vertical, so its acute angle relative to the roughly horizontal ground is about 65°.

---

## BATCH 3

### #1: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 100.0
- Ratio (Pred/GT): 4.44× (OVER)
- Error: 344.4%

**Reasoning Trace:**
> The marked lower brace appears to meet the slanted main panel at about a right angle, slightly obtuse in the image, so the visible joint angle is roughly 100 degrees.

---

### #2: `M-angle-image3.jpg`

**Prediction Metrics:**
- Ground Truth: 18.85
- Prediction: 58.0
- Ratio (Pred/GT): 3.08× (OVER)
- Error: 207.7%

**Reasoning Trace:**
> The marked acute angle between the horizontal red reference line and the slanted segment appears to be a little under 60 degrees.

---

### #3: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 63.0
- Ratio (Pred/GT): 2.23× (OVER)
- Error: 122.6%

**Reasoning Trace:**
> The highlighted contact angle appears to be between the package’s slanted side edge and the floor; that edge is roughly a bit over 60° from horizontal.

---

### #4: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 17.0
- Ratio (Pred/GT): 2.21× (OVER)
- Error: 120.8%

**Reasoning Trace:**
> The highlighted hinge shows the pedal surface only slightly tilted relative to the nearly horizontal reference/linkage, making a small acute angle of roughly the mid-teens.

---

### #5: `V-angle-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 95.0
- Ratio (Pred/GT): 2.02× (OVER)
- Error: 102.1%

**Reasoning Trace:**
> The two visible segments at the marked joint form a near right-angle V, appearing slightly wider than 90°.

---

### #6: `V-angle-image59-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 90.0
- Ratio (Pred/GT): 1.91× (OVER)
- Error: 91.5%

**Reasoning Trace:**
> The highlighted point is a corner of the rectangular ottoman/cushion, where two adjacent edges meet at approximately a right angle.

---

### #7: `P-angle-image9.jpg`

**Prediction Metrics:**
- Ground Truth: 37.2
- Prediction: 64.0
- Ratio (Pred/GT): 1.72× (OVER)
- Error: 72.0%

**Reasoning Trace:**
> The leaning wooden plank forms an acute angle with the ground that looks a little over 60 degrees, roughly in the mid-60s.

---

### #8: `V-angle-image41.jpg`

**Prediction Metrics:**
- Ground Truth: 70.9
- Prediction: 113.0
- Ratio (Pred/GT): 1.59× (OVER)
- Error: 59.4%

**Reasoning Trace:**
> The marked corner appears to show the exterior angle: the right leg is roughly 70° above horizontal and the lower bar’s extension is about 40° below horizontal, so the angle is about 110–115°.

---

### #9: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 70.0
- Ratio (Pred/GT): 1.46× (OVER)
- Error: 45.8%

**Reasoning Trace:**
> The highlighted joint forms an acute angle between the long pole and the short lower connector/base piece; visually it looks a bit more than 60° and close to 70°.

---

### #10: `V-angle-image33.jpg`

**Prediction Metrics:**
- Ground Truth: 40.75
- Prediction: 58.0
- Ratio (Pred/GT): 1.42× (OVER)
- Error: 42.3%

**Reasoning Trace:**
> The marked angle is the acute angle between the slanted cushion side and the floor, which visually appears a bit under 60 degrees.

---

# GEMINI MODEL

## BATCH 1

### #1: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 165.0
- Ratio (Pred/GT): 5.83× (OVER)
- Error: 483.0%

**Reasoning Trace:**
> The marked angle consists of two red line segments originating from the bottom corner of the blue box. The upward segment follows the edge of the box, which is tilted at an angle of approximately 69 degrees above the horizontal. The downward segment points almost straight down but slightly to the left, at an angle of roughly 263 degrees (or -97 degrees) from the positive horizontal axis. Calculating the angle between these two vectors gives approximately 166 degrees. I will estimate it at 165 degrees.

---

### #2: `V-angle-image32.jpg`

**Prediction Metrics:**
- Ground Truth: 37.6
- Prediction: 126.0
- Ratio (Pred/GT): 3.35× (OVER)
- Error: 235.1%

**Reasoning Trace:**
> The marked angle is formed between the upward-left direction of the wooden stick and a perfectly vertical line dropping downwards. The stick extends from roughly pixel (182, 443) to (686, 803), giving it a slope of approximately 360/504 ≈ 0.714. This corresponds to an angle of about 35.5° with the horizontal. The angle between the upward-left stick direction and the downward vertical direction is therefore 90° + 35.5° = 125.5°.

---

### #3: `B-angle-image3.jpg`

**Prediction Metrics:**
- Ground Truth: 44.0
- Prediction: 72.0
- Ratio (Pred/GT): 1.64× (OVER)
- Error: 63.6%

**Reasoning Trace:**
> By visually measuring the angle between the two red lines in the image, we can estimate its value. The reference line is not perfectly horizontal but dips slightly downwards by about 15 degrees relative to the true horizontal of the image. The line following the metal leg rises steeply at approximately 55-60 degrees relative to the true horizontal. Adding these two angles together (since they are on opposite sides of the true horizontal) gives an estimated total angle of roughly 70 to 75 degrees.

---

### #4: `P-angle-image15.jpg`

**Prediction Metrics:**
- Ground Truth: 37.0
- Prediction: 60.0
- Ratio (Pred/GT): 1.62× (OVER)
- Error: 62.2%

**Reasoning Trace:**
> The marked angle is formed between an imaginary horizontal reference line and the sloping wooden leg. By observing the image and estimating the pixel coordinates along the edges of the leg, we can determine its slope. The leg rises approximately 1.75 units for every 1 unit it moves horizontally. Calculating the arctangent of this rise-over-run ratio (atan(1.75)) gives an angle of approximately 60 degrees.

---

### #5: `V-angle-image68-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 69.5
- Prediction: 105.0
- Ratio (Pred/GT): 1.51× (OVER)
- Error: 51.1%

**Reasoning Trace:**
> The marked angle is the external, obtuse angle between the floor and the back surface of the canvas. The canvas is leaning against the step/wall behind it. By estimating the lean of the canvas from the vertical to be approximately 15 degrees, the angle it makes with the floor on the inside is roughly 75 degrees. The marked external angle would therefore be about 180 - 75 = 105 degrees.

---

### #6: `V-angle-image71.jpg`

**Prediction Metrics:**
- Ground Truth: 40.35
- Prediction: 57.0
- Ratio (Pred/GT): 1.41× (OVER)
- Error: 41.3%

**Reasoning Trace:**
> By estimating the coordinates of the hinge vertex and points along the edges of the base and screen, we can calculate the vectors for both edges. The base edge lies at roughly a -7 degree angle relative to the horizontal, while the screen edge is at approximately a -63 degree angle. Subtracting these gives an internal angle of approximately 56 to 57 degrees.

---

### #7: `M-angle-image11.jpg`

**Prediction Metrics:**
- Ground Truth: 70.95
- Prediction: 97.0
- Ratio (Pred/GT): 1.37× (OVER)
- Error: 36.7%

**Reasoning Trace:**
> Based on a visual analysis of the red markings in the image, the horizontal line appears to be drawn perfectly level with the image frame (0 degrees). The inclined line, which follows the back of the computer stand, can be estimated by picking two points. The intersection point is roughly at pixel coordinates (436, 606), and the top end of the red line is near (447, 517). This indicates a vertical rise of 89 pixels for a horizontal run of 11 pixels. The acute angle of this slope relative to the horizontal is arctan(89/11), which is approximately 83 degrees. The red arc marks the obtuse angle between the left-pointing horizontal line and the upward-pointing inclined line, which is calculated as 180 - 83 = 97 degrees.

---

### #8: `V-angle-image66-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 90.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.1%

**Reasoning Trace:**
> The red arc indicates the angle between the bottom edge and the side edge of the green board's frame. Because the board is rectangular, the internal angle at any of its corners is a right angle, or 90 degrees.

---

### #9: `V-angle-image66.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 90.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.1%

**Reasoning Trace:**
> The marked angle is at the corner of a rectangular board's frame. Because the frame is rectangular, the angle where the two side pieces meet at the corner is a right angle.

---

### #10: `P-angle-image7.jpg`

**Prediction Metrics:**
- Ground Truth: 22.8
- Prediction: 31.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.0%

**Reasoning Trace:**
> By determining the coordinates of points along the stone surface and the bottom edge of the purple object, we can calculate their respective slopes in the image. The stone surface has a slight downward slope of approximately 2.5 degrees relative to the image's horizontal axis. The bottom edge of the purple object slopes upwards at about 28.5 degrees. The relative angle between them is the sum of these two angles, which is approximately 31 degrees.

---

## BATCH 2

### #1: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 90.0
- Ratio (Pred/GT): 4.00× (OVER)
- Error: 300.0%

**Reasoning Trace:**
> The red arc marks the angle at the corner of the wooden leg, specifically between the long side of the leg and its flat end. Since the leg is shaped like a rectangular prism, the angle between these two adjacent faces is a right angle.

---

### #2: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 110.0
- Ratio (Pred/GT): 3.89× (OVER)
- Error: 288.7%

**Reasoning Trace:**
> The marked angle is indicated by two red line segments originating from the bottom corner of the blue box. The first segment follows the bottom edge of the box, extending left and upwards at an angle of approximately 27 degrees relative to a horizontal line. The second segment points downwards and slightly left, at an angle of roughly 83 degrees below the horizontal. By adding these two angles together (27 + 83), we can estimate the total marked angle to be around 110 degrees.

---

### #3: `V-angle-image32.jpg`

**Prediction Metrics:**
- Ground Truth: 37.6
- Prediction: 124.5
- Ratio (Pred/GT): 3.31× (OVER)
- Error: 231.1%

**Reasoning Trace:**
> The red mark indicates the angle between a vertical line pointing downwards and the upward-left direction of the wooden stick. By measuring the stick's slope in the image, it forms an angle of approximately 34.5 degrees with the horizontal. The marked angle is obtuse, consisting of the 90-degree angle between the horizontal and the downward vertical, plus the 34.5-degree angle of the stick above the horizontal. Therefore, the angle is roughly 90 + 34.5 = 124.5 degrees.

---

### #4: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 20.0
- Ratio (Pred/GT): 2.60× (OVER)
- Error: 159.7%

**Reasoning Trace:**
> By analyzing the image and estimating pixel coordinates of the marked red lines, the top line appears approximately horizontal. The bottom line originates at the vertex roughly at (655, 666) and passes through a point around (625, 677). This relative displacement gives a slope of roughly 11/30 (vertical change / horizontal change), which is approximately 0.367. Taking the arctangent of this slope yields an angle of roughly 20 degrees.

---

### #5: `V-angle-image72-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 62.6
- Prediction: 118.0
- Ratio (Pred/GT): 1.88× (OVER)
- Error: 88.5%

**Reasoning Trace:**
> The marked angle is between the slanted table leg and the horizontal floor on the inside (right side of the leg in the image). By identifying two points along the center line of the leg (approximately at the top joint and just above the bottom foot), we can determine its slope. The leg leans to the left, and its angle relative to a perfectly horizontal line (0 degrees) can be calculated using the arctangent of its vertical to horizontal pixel differences. The leg is roughly 28-30 degrees off from the vertical, making the obtuse angle with the floor approximately 118 degrees.

---

### #6: `P-angle-image30.jpg`

**Prediction Metrics:**
- Ground Truth: 27.45
- Prediction: 45.0
- Ratio (Pred/GT): 1.64× (OVER)
- Error: 63.9%

**Reasoning Trace:**
> By analyzing the pixel coordinates of the red lines, the vertex of the angle is approximately at (443, 555). The horizontal line is drawn straight to the left. The sloping red line follows the pipe and ends at approximately (357, 467). The vertical difference is 555 - 467 = 88 pixels, and the horizontal difference is 443 - 357 = 86 pixels. The ratio of these differences is approximately 1, which corresponds to an angle of 45 degrees.

---

### #7: `P-angle-image15.jpg`

**Prediction Metrics:**
- Ground Truth: 37.0
- Prediction: 57.0
- Ratio (Pred/GT): 1.54× (OVER)
- Error: 54.1%

**Reasoning Trace:**
> To estimate the marked angle, we can trace the central axis of the wooden stick. The lower end of the stick is approximately at pixel coordinates (398, 517) and the upper end near the central joint is at (519, 329). The differences in coordinates are dx = 121 and dy = 188. Calculating the angle relative to the horizontal gives arctan(188 / 121) ≈ 57 degrees.

---

### #8: `P-angle-image20.jpg`

**Prediction Metrics:**
- Ground Truth: 63.0
- Prediction: 96.0
- Ratio (Pred/GT): 1.52× (OVER)
- Error: 52.4%

**Reasoning Trace:**
> The angle is marked by the red lines. To estimate it, I measure the angle between the two drawn segments in the 2D image. The vertex is approximately at pixel coordinates (556, 459). The upper arm follows the edge of the orange box, ending around (541, 419), which corresponds to a vector of roughly (-15, 40) in standard Cartesian coordinates (y-axis up). The lower reference arm points left and slightly down, ending around (513, 481), corresponding to a vector of roughly (-43, -22). Calculating the angle between these two vectors yields approximately 96 degrees. Although the box's actual incline from true horizontal is around 68-70 degrees, the prompt specifies estimating the angle 'relative to the shown reference line', which is drawn with a downward slant.

---

### #9: `V-angle-image68-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 69.5
- Prediction: 105.0
- Ratio (Pred/GT): 1.51× (OVER)
- Error: 51.1%

**Reasoning Trace:**
> The marked red arc indicates the dihedral angle between the horizontal floor and the back surface of the canvas. The canvas is resting on the floor and leaning back against a vertical step or wall. A typical gentle lean to keep an object stable is around 10 to 20 degrees from the vertical. Assuming a lean of roughly 15 degrees, the obtuse angle formed with the floor behind it would be 90 + 15 = 105 degrees.

---

### #10: `V-angle-image33.jpg`

**Prediction Metrics:**
- Ground Truth: 40.75
- Prediction: 60.0
- Ratio (Pred/GT): 1.47× (OVER)
- Error: 47.2%

**Reasoning Trace:**
> The red arc marks the angle of inclination of the cushion relative to the horizontal floor. The cushion rests against a blue pallet, and evaluating the slope of this setup shows that the vertical height is roughly twice the horizontal base. This steep incline is clearly greater than 45 degrees and aligns well with an angle of approximately 60 degrees.

---

## BATCH 3

### #1: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 90.0
- Ratio (Pred/GT): 3.18× (OVER)
- Error: 218.0%

**Reasoning Trace:**
> The red lines highlight a corner of the rectangular product box. The adjacent faces of a rectangular box meet at a right angle.

---

### #2: `V-angle-image34.jpg`

**Prediction Metrics:**
- Ground Truth: 40.5
- Prediction: 90.0
- Ratio (Pred/GT): 2.22× (OVER)
- Error: 122.2%

**Reasoning Trace:**
> The marked angle is located at the corner of the book's cover. Since a book cover is rectangular, the angle between its adjacent edges is a right angle, which is 90 degrees.

---

### #3: `P-angle-image30.jpg`

**Prediction Metrics:**
- Ground Truth: 27.45
- Prediction: 45.0
- Ratio (Pred/GT): 1.64× (OVER)
- Error: 63.9%

**Reasoning Trace:**
> The marked angle is formed by a horizontal reference line and a slanted line that follows the downward slope of the tube. By visually estimating the horizontal and vertical components of the slanted red line from its vertex, the horizontal distance (run) appears roughly equal to the vertical distance (rise). A 1:1 ratio of rise to run corresponds to an angle of 45 degrees.

---

### #4: `V-angle-image29.jpg`

**Prediction Metrics:**
- Ground Truth: 64.5
- Prediction: 105.0
- Ratio (Pred/GT): 1.63× (OVER)
- Error: 62.8%

**Reasoning Trace:**
> The marked angle is located at the bottom tip of the front chair leg. By measuring the two red lines forming the 'V' shape in the 2D image plane, the upper line roughly aligns with the slanted chair leg, and the lower line points downwards and to the left. Calculating the angle between these two designated directions yields an obtuse angle of approximately 105 degrees.

---

### #5: `P-angle-image15.jpg`

**Prediction Metrics:**
- Ground Truth: 37.0
- Prediction: 60.0
- Ratio (Pred/GT): 1.62× (OVER)
- Error: 62.2%

**Reasoning Trace:**
> By estimating the pixel coordinates of the wooden stick's centerline, the bottom tip is approximately at (406, 517) and the point where it intersects the other sticks is near (504, 344). The change in the y-direction (dy) is roughly 173 pixels, and the change in the x-direction (dx) is roughly 98 pixels. The slope of the stick relative to the horizontal is 173 / 98 ≈ 1.765. Taking the arctangent of this slope gives an angle of approximately 60.5 degrees. Thus, the marked angle is closest to 60 degrees.

---

### #6: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 33.0
- Ratio (Pred/GT): 1.47× (OVER)
- Error: 46.7%

**Reasoning Trace:**
> The red arc marks the angle between the stool's leg and the floor. Assuming the floor corresponds to the horizontal axis of the image, we can measure the angle of the leg's long edge. Taking points along the top visible edge of the bottom leg, such as approximately (334, 694) and (545, 831), we find the slope is roughly (831 - 694) / (545 - 334) = 137 / 211 ≈ 0.649. The angle is arctan(0.649), which is approximately 33 degrees.

---

### #7: `V-angle-image32.jpg`

**Prediction Metrics:**
- Ground Truth: 37.6
- Prediction: 55.0
- Ratio (Pred/GT): 1.46× (OVER)
- Error: 46.3%

**Reasoning Trace:**
> The red marking indicates the angle between the slanted wooden stick and a perfectly vertical line. To estimate this, I can measure the slope of the stick using its endpoints in the image. The top-left end of the stick is approximately at pixel coordinates (182, 451), and the bottom-right end resting on the scale is at roughly (678, 796). The difference in x is 496 and the difference in y is 345. The angle the stick makes with the vertical is calculated as atan(dx/dy) = atan(496/345), which yields approximately 55.2 degrees. The red 'V' shape clearly denotes the acute angle, which aligns with this estimate.

---

### #8: `V-angle-image71.jpg`

**Prediction Metrics:**
- Ground Truth: 40.35
- Prediction: 59.0
- Ratio (Pred/GT): 1.46× (OVER)
- Error: 46.2%

**Reasoning Trace:**
> By tracing the visible side edges of the laptop, we can estimate the marked angle. The vertex (hinge) is approximately at pixel coordinates (336, 722). A point along the base edge is at roughly (508, 709), giving it a slight upward angle of about 4.3 degrees from horizontal. A point along the lid edge is near (527, 349), giving it an angle of about 62.9 degrees from horizontal. Subtracting these angles (62.9 - 4.3) yields an estimated 2D opening angle of approximately 58.6 degrees.

---

### #9: `P-angle-image18.jpg`

**Prediction Metrics:**
- Ground Truth: 37.25
- Prediction: 54.0
- Ratio (Pred/GT): 1.45× (OVER)
- Error: 45.0%

**Reasoning Trace:**
> The angle is marked between a perfectly horizontal line and an inclined yellow rope. Measuring the coordinates in the image, the vertex is at approximately (348, 453). A point further up the rope is at approximately (448, 313). The change in x (dx) is 100 pixels, and the change in y (dy) is 140 pixels. The slope (dy/dx) is 1.4. The angle is arctan(1.4), which is approximately 54.5 degrees. I will estimate it as 54 degrees.

---

### #10: `B-angle-image3.jpg`

**Prediction Metrics:**
- Ground Truth: 44.0
- Prediction: 60.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.4%

**Reasoning Trace:**
> By measuring the slope of the metal leg in the image plane, it rises roughly 1.7 pixels for every 1 pixel it moves horizontally, which corresponds to an angle of arctan(1.7) ≈ 60 degrees. Furthermore, the other visible leg of the cross-structure declines at approximately the same angle (60 degrees) to the horizontal, strongly suggesting the object is constructed with 60-degree intersecting angles. Although the hand-drawn red reference line has a slight downward tilt, it is intended to represent the horizontal ground plane. Therefore, the intended marked angle is 60 degrees.

---

# GEMINI-ROBOTICS MODEL

## BATCH 1

### #1: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 165.0
- Ratio (Pred/GT): 21.43× (OVER)
- Error: 2042.9%

**Reasoning Trace:**
> The marked angle is between the top horizontal-ish surface of the pedal and its downward-sloping side edge. Visually, the angle is slightly obtuse, estimated at approximately 165 degrees based on the small deflection from a straight line.

---

### #2: `V-angle-image32.jpg`

**Prediction Metrics:**
- Ground Truth: 37.6
- Prediction: 175.0
- Ratio (Pred/GT): 4.65× (OVER)
- Error: 365.4%

**Reasoning Trace:**
> The marked point is located on a long wooden stick. The question asks for the bend or joint angle at that point. Upon close inspection of the stick near the red mark, there is no distinct sharp bend or joint visible; the stick appears essentially straight at that location. In problems like these, a 'straight joint' or bend angle is typically close to 180 degrees. Alternatively, if there is a slight, almost imperceptible bend intended by the image markings, it is very close to 180 degrees.

---

### #3: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 90.0
- Ratio (Pred/GT): 4.00× (OVER)
- Error: 300.0%

**Reasoning Trace:**
> The marked angle is at the joint where the support leg meets the main body of the foldable wooden piece. Based on visual estimation from the provided perspective, the angle between the leg and the brace it attaches to looks close to a right angle, but slightly obtuse due to perspective, typically designed to be around 90-100 degrees for stability. Looking closely at the vertex, 90.0 is a reasonable estimate.

---

### #4: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 110.0
- Ratio (Pred/GT): 3.89× (OVER)
- Error: 288.7%

**Reasoning Trace:**
> The marked angle is formed between a vertical ray extending downwards and a ray following the bottom-right edge of the leaning product box. The angle appears obtuse, roughly estimated around 110-120 degrees relative to the downward vertical direction, or specifically the angle shown at the vertex is being measured.

---

### #5: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 150.0
- Ratio (Pred/GT): 3.12× (OVER)
- Error: 212.5%

**Reasoning Trace:**
> The marked angle is between the long handle of the mop/broom and its small base piece sitting on the floor. Based on visual estimation, the handle is at an obtuse angle relative to the base piece, appearing to be roughly 150 degrees.

---

### #6: `V-angle-image69.jpg`

**Prediction Metrics:**
- Ground Truth: 52.0
- Prediction: 115.0
- Ratio (Pred/GT): 2.21× (OVER)
- Error: 121.2%

**Reasoning Trace:**
> The marked angle is between the bottom of the red board and the horizontal floor. Estimating the slope, the board is leaning at a fairly steep angle. The acute interior angle between the board and floor appears to be roughly 65-70 degrees. The marked arc indicates the supplementary angle outside, which is roughly 110-120 degrees. Based on direct observation of the vertex and arc shape, 115 degrees is a solid estimate.

---

### #7: `V-angle-image59-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 90.0
- Ratio (Pred/GT): 1.91× (OVER)
- Error: 91.5%

**Reasoning Trace:**
> The marked angle is at the corner of a rectangular block-like object, likely a furniture piece. Given its standard shape, the joint angle between its adjacent sides is approximately 90 degrees.

---

### #8: `V-angle-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 90.0
- Ratio (Pred/GT): 1.91× (OVER)
- Error: 91.5%

**Reasoning Trace:**
> The marked point is between the side and the bottom edge of the ottoman. Assuming it is a cuboid object, the standard angle between adjacent faces is 90 degrees.

---

### #9: `V-angle-image72-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 62.6
- Prediction: 115.0
- Ratio (Pred/GT): 1.84× (OVER)
- Error: 83.7%

**Reasoning Trace:**
> The angle between the inclined table leg and the horizontal ground surface appears moderately obtuse, estimated to be around 115 degrees.

---

### #10: `V-angle-image72.jpg`

**Prediction Metrics:**
- Ground Truth: 62.6
- Prediction: 110.0
- Ratio (Pred/GT): 1.76× (OVER)
- Error: 75.7%

**Reasoning Trace:**
> The marked joint is between the sloping leg of the small table and its horizontal foot. Visually, the angle inside the bend looks obtuse, slightly more than 90 degrees, roughly estimated between 105 and 115 degrees based on the tilt.

---

## BATCH 2

### #1: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 168.0
- Ratio (Pred/GT): 21.82× (OVER)
- Error: 2081.8%

**Reasoning Trace:**
> The marked angle is between the flat upper surface of the pedal and its downward-sloping side edge. Looking at the image, the horizontal reference line and the downward stroke define a wide obtuse angle, approximately 165 to 175 degrees, or its supplement if considering the 'bend'. Given the shape, it looks to be roughly 168 degrees.

---

### #2: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 165.0
- Ratio (Pred/GT): 5.83× (OVER)
- Error: 483.0%

**Reasoning Trace:**
> The marked angle consists of two segments near the corner of the tilted box. One segment is nearly vertical, while the other is tilted along the edge of the box, creating an obtuse angle. Estimating based on visual orientation, the angle is approximately 165 degrees.

---

### #3: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 90.0
- Ratio (Pred/GT): 4.00× (OVER)
- Error: 300.0%

**Reasoning Trace:**
> The marked joint is between the leg and its support structure. Based on the common manufacturing of such items, these joints are typically 90 degrees, although the perspective makes it appear different.

---

### #4: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 150.0
- Ratio (Pred/GT): 3.12× (OVER)
- Error: 212.5%

**Reasoning Trace:**
> The marked angle is between the pole and its base. Looking at the tilt of the pole relative to the base connector, it appears to be a wide obtuse angle, estimated at roughly 150 degrees.

---

### #5: `V-angle-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 130.0
- Ratio (Pred/GT): 2.77× (OVER)
- Error: 176.6%

**Reasoning Trace:**
> The marked angle is between the bottom surface of the ottoman and the horizontal floor. Estimating the tilt, the angle from the floor to the ottoman's vertical-ish face is typically around 120-140 degrees for such items in these contexts, specifically looking obtuse here.

---

### #6: `B-angle-image1.jpg`

**Prediction Metrics:**
- Ground Truth: 52.8
- Prediction: 125.0
- Ratio (Pred/GT): 2.37× (OVER)
- Error: 136.7%

**Reasoning Trace:**
> The reference line is horizontal. The handle of the hose reel cart is angled upwards and to the left from the right-hand horizontal axis. Visually, the angle from the positive horizontal axis is obtuse. Measured counter-clockwise, it appears to be approximately 120-130 degrees. Looking closely at the arc position, it represents the exterior-type angle starting from horizontal right, which seems to be around 125 degrees.

---

### #7: `V-angle-image59-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 90.0
- Ratio (Pred/GT): 1.91× (OVER)
- Error: 91.5%

**Reasoning Trace:**
> The marked point is located at the corner of a rectangular cushion. Visually, the corner where the two edges meet appears to be a standard right angle, approximately 90 degrees, modified slightly by its perspective in the image.

---

### #8: `V-angle-image72-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 62.6
- Prediction: 115.0
- Ratio (Pred/GT): 1.84× (OVER)
- Error: 83.7%

**Reasoning Trace:**
> The marked angle is formed between the table leg and the horizontal floor. Estimating visually, the table leg forms an angle of approximately 115 degrees with the floor to its right side, where the marking is.

---

### #9: `V-angle-image72.jpg`

**Prediction Metrics:**
- Ground Truth: 62.6
- Prediction: 110.0
- Ratio (Pred/GT): 1.76× (OVER)
- Error: 75.7%

**Reasoning Trace:**
> The marked angle is at the bottom of the table leg where it meets the ground extension. The leg is tilted outwards, and the arc marks the angle between the leg and the imaginary horizontal line extending outwards, which appears to be obtuse, estimated at around 110 degrees.

---

### #10: `V-angle-image65.jpg`

**Prediction Metrics:**
- Ground Truth: 62.75
- Prediction: 110.0
- Ratio (Pred/GT): 1.75× (OVER)
- Error: 75.3%

**Reasoning Trace:**
> The marked angle is between the floor and the side of the box. Since the box is leaning away from the side where the angle is marked, it creates an obtuse angle slightly greater than 90 degrees. Visually, it appears to be approximately 110 degrees.

---

## BATCH 3

### #1: `V-angle-image31.jpg`

**Prediction Metrics:**
- Ground Truth: 22.5
- Prediction: 110.0
- Ratio (Pred/GT): 4.89× (OVER)
- Error: 388.9%

**Reasoning Trace:**
> The marked angle is at the joint between the table leg and the floor, or potentially indicating the angle of bend if parts were meeting. Based on the curve of the red line, it seems to suggest an obtuse angle between the inner surface of the table leg and the imaginary baseline or ground, roughly 120-140 degrees depending on perspective. Looking closely at typical furniture angles and the position of the marker, I will estimate it near 110 degrees.

---

### #2: `V-angle-image74.jpg`

**Prediction Metrics:**
- Ground Truth: 28.3
- Prediction: 105.0
- Ratio (Pred/GT): 3.71× (OVER)
- Error: 271.0%

**Reasoning Trace:**
> The marked angle is between a vertical line segment and the bottom edge of the tilted box. Given the box's tilt relative to the floor, the interior angle at that marked junction appears to be roughly 100 to 110 degrees. Based on visual estimation, it is slightly obtuse.

---

### #3: `V-angle-image39.jpg`

**Prediction Metrics:**
- Ground Truth: 48.0
- Prediction: 145.0
- Ratio (Pred/GT): 3.02× (OVER)
- Error: 202.1%

**Reasoning Trace:**
> The marked joint angle is between the slanted pole and its base component. Based on the visible inclination, the handle is at roughly a 145 to 155 degree angle from the base's straight extension, or alternatively, looking at the angle from the floor, it appears to be approximately 145 degrees.

---

### #4: `V-angle-image59.jpg`

**Prediction Metrics:**
- Ground Truth: 47.0
- Prediction: 135.0
- Ratio (Pred/GT): 2.87× (OVER)
- Error: 187.2%

**Reasoning Trace:**
> The marked angle is between the floor and the slanted bottom of the object. Based on the orientation of the object tilted relative to the horizontal floor, the internal angle is approximately 135 degrees, or its supplementary angle of 45 degrees. Given the placement of the arc, it points to the obtuse angle between the floor and the object's bottom face.

---

### #5: `M-angle-image8.jpg`

**Prediction Metrics:**
- Ground Truth: 7.7
- Prediction: 15.0
- Ratio (Pred/GT): 1.95× (OVER)
- Error: 94.8%

**Reasoning Trace:**
> The marked angle is formed between the approximately flat top surface of the pedal and its downward-sloping side edge. Visually, the angle relative to the horizontal extension is small, likely between 10 and 20 degrees.

---

### #6: `V-angle-image29.jpg`

**Prediction Metrics:**
- Ground Truth: 64.5
- Prediction: 105.0
- Ratio (Pred/GT): 1.63× (OVER)
- Error: 62.8%

**Reasoning Trace:**
> The angle requested is between the backrest part and the seat of the chair. Based on typical chair designs, this angle is slightly greater than 90 degrees, and visually it appears to be around 100-110 degrees. Without explicit marking, the most standard chair angle estimate is used.

---

### #7: `P-angle-image15.jpg`

**Prediction Metrics:**
- Ground Truth: 37.0
- Prediction: 60.0
- Ratio (Pred/GT): 1.62× (OVER)
- Error: 62.2%

**Reasoning Trace:**
> The marked incline angle is between the thin wooden leg and the ground. Based on visual estimation, the angle appears steeper than 45 degrees but well below vertical (90 degrees), placing it roughly around 60 degrees from the horizontal ground surface.

---

### #8: `M-angle-image10.jpg`

**Prediction Metrics:**
- Ground Truth: 17.5
- Prediction: 25.0
- Ratio (Pred/GT): 1.43× (OVER)
- Error: 42.9%

**Reasoning Trace:**
> The marked incline angle is relative to a horizontal reference line indicated in red near the top right corner of the frame. By observing the orientation of the sloped frame edge compared to the horizontal, the angle is estimated to be approximately 25 degrees.

---

### #9: `V-angle-image66-pov2.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 90.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.1%

**Reasoning Trace:**
> The marked angle is at the corner where the horizontal and vertical frames of the chalkboard meet, which forms a right angle typical of rectangular boards.

---

### #10: `V-angle-image66.jpg`

**Prediction Metrics:**
- Ground Truth: 66.15
- Prediction: 90.0
- Ratio (Pred/GT): 1.36× (OVER)
- Error: 36.1%

**Reasoning Trace:**
> The marked point is at the corner of a rectangular board frame, where two perpendicular frame pieces meet. Such corners are typically designed to be right angles.

---

