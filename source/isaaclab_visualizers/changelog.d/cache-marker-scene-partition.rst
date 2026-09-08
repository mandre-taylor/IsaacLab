Fixed
^^^^^

* Fixed :class:`~isaaclab_visualizers.kit.kit_visualization_markers.KitVisualizationMarkers`
  rebuilding its scene-partition tokens on every frame. Marker ownership is now cached and the
  ``primvars:omni:scenePartition`` primvar is only re-authored when the environment IDs change,
  removing a per-frame device synchronization and one token string per marker. This noticeably
  improves throughput for camera tasks at high environment counts.
