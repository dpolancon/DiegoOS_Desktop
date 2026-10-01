# Literature to Code Mapping

This document maps the academic research in `/papers` to the implementation in `/src`. 
When implementing a module, read the corresponding paper first.

## Phase 1: Foundation & Data Extraction

### 1. Video Ingestion & Frame Extraction
*   **Concept:** Efficient decoding of high-res video without bottlenecking the GPU.
*   **Reference Paper:** `papers/cv_drone_tracking/efficient_video_decoding.pdf` (Hypothetical)
*   **Implementation:** `src/ingestion/video_reader.py`
*   **Key Takeaway:** Use `Decord` instead of `OpenCV` `VideoCapture` for 4K to bypass CPU bottlenecks.

### 2. Pitch Calibration (Homography)
*   **Concept:** Mapping 2D image coordinates to 2D world (pitch) coordinates using projective geometry.
*   **Reference Paper:** `papers/homography_sports/automated_pitch_calibration.pdf`
*   **Implementation:** `src/preprocessing/homography.py`
*   **Key Math:** `cv2.getPerspectiveTransform(src_points, dst_points)` -> `cv2.warpPerspective()`
*   **Validation:** See `tests/test_homography.py` to ensure mapping error is < 0.5 meters.

### 3. Small Object Detection (Drone View)
*   **Concept:** Standard YOLO fails on tiny players. We need feature pyramid adjustments or specific loss functions.
*   **Reference Paper:** `papers/yolo_small_objects/anchor_free_tiny_detection.pdf`
*   **Implementation:** `src/detection/yolo_trainer.py` & `configs/detection.yaml`
*   **Key Takeaway:** Increase the resolution of the P3/P4 detection heads in the YOLO config; add Mosaic augmentation.

### 4. Multi-Object Tracking (MOT)
*   **Concept:** Associating detections across frames using motion prediction and appearance features.
*   **Reference Paper:** `papers/multi_object_tracking/deep_sort_deep_association.pdf`
*   **Implementation:** `src/tracking/mot_engine.py`
*   **Key Math:** Kalman Filter for state prediction; Hungarian algorithm for linear assignment; Cosine distance for Re-ID.