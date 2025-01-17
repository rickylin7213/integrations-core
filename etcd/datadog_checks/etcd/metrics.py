METRIC_MAP = {
    'etcd_debugging_mvcc_db_compaction_keys_total': 'debugging.mvcc.db.compaction.keys.total',
    'etcd_debugging_mvcc_db_compaction_pause_duration_milliseconds': (
        'debugging.mvcc.db.compaction.pause.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_db_compaction_total_duration_milliseconds': (
        'debugging.mvcc.db.compaction.total.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_db_total_size_in_bytes': 'debugging.mvcc.db.total.size.in_bytes',
    'etcd_debugging_mvcc_delete_total': 'debugging.mvcc.delete.total',
    'etcd_debugging_mvcc_events_total': 'debugging.mvcc.events.total',
    'etcd_debugging_mvcc_index_compaction_pause_duration_milliseconds': (
        'debugging.mvcc.index.compaction.pause.duration.milliseconds'
    ),
    'etcd_debugging_mvcc_keys_total': 'debugging.mvcc.keys.total',
    'etcd_debugging_mvcc_pending_events_total': 'debugging.mvcc.pending.events.total',
    'etcd_debugging_mvcc_put_total': 'debugging.mvcc.put.total',
    'etcd_debugging_mvcc_range_total': 'debugging.mvcc.range.total',
    'etcd_debugging_mvcc_slow_watcher_total': 'debugging.mvcc.slow_watcher.total',
    'etcd_debugging_mvcc_txn_total': 'debugging.mvcc.txn.total',
    'etcd_debugging_mvcc_watch_stream_total': 'debugging.mvcc.watch_stream.total',
    'etcd_debugging_mvcc_watcher_total': 'debugging.mvcc.watcher.total',
    'etcd_debugging_server_lease_expired_total': 'debugging.server.lease.expired.total',
    'etcd_debugging_snap_save_marshalling_duration_seconds': 'debugging.snap.save.marshalling.duration.seconds',
    'etcd_debugging_snap_save_total_duration_seconds': 'debugging.snap.save.total.duration.seconds',
    'etcd_debugging_store_expires_total': 'debugging.store.expires.total',
    'etcd_debugging_store_reads_total': 'debugging.store.reads.total',
    'etcd_debugging_store_watch_requests_total': 'debugging.store.watch.requests.total',
    'etcd_debugging_store_watchers': 'debugging.store.watchers',
    'etcd_debugging_store_writes_total': 'debugging.store.writes.total',
    'etcd_disk_backend_commit_duration_seconds': 'disk.backend.commit.duration.seconds',
    'etcd_disk_backend_snapshot_duration_seconds': 'disk.backend.snapshot.duration.seconds',
    'etcd_disk_wal_fsync_duration_seconds': 'disk.wal.fsync.duration.seconds',
    'etcd_disk_wal_write_bytes_total': 'disk.wal.write.bytes.total',
    'etcd_grpc_proxy_cache_hits_total': 'grpc.proxy.cache.hits.total',
    'etcd_grpc_proxy_cache_keys_total': 'grpc.proxy.cache.keys.total',
    'etcd_grpc_proxy_cache_misses_total': 'grpc.proxy.cache.misses.total',
    'etcd_grpc_proxy_events_coalescing_total': 'grpc.proxy.events.coalescing.total',
    'etcd_grpc_proxy_watchers_coalescing_total': 'grpc.proxy.watchers.coalescing.total',
    'etcd_mvcc_db_total_size_in_bytes': 'debugging.mvcc.db.total.size.in_bytes',
    'etcd_mvcc_db_total_size_in_use_in_bytes': 'mvcc.db.total.size.in_use.bytes',
    'etcd_mvcc_delete_total': 'debugging.mvcc.delete.total',
    'etcd_mvcc_put_total': 'debugging.mvcc.put.total',
    'etcd_mvcc_range_total': 'debugging.mvcc.range.total',
    'etcd_mvcc_txn_total': 'debugging.mvcc.txn.total',
    'etcd_server_go_version': 'server.go_version',
    'etcd_server_has_leader': 'server.has_leader',
    'etcd_server_health_failures': 'server.health.failures.total',
    'etcd_server_health_success': 'server.health.success.total',
    'etcd_server_heartbeat_send_failures_total': 'server.heartbeat.send.failures.total',
    'etcd_server_is_leader': 'server.is_leader',
    'etcd_server_leader_changes_seen_total': 'server.leader.changes.seen.total',
    'etcd_server_lease_expired_total': 'server.lease.expired.total',
    'etcd_server_proposals_applied_total': 'server.proposals.applied.total',
    'etcd_server_proposals_committed_total': 'server.proposals.committed.total',
    'etcd_server_proposals_failed_total': 'server.proposals.failed.total',
    'etcd_server_proposals_pending': 'server.proposals.pending',
    'etcd_server_quota_backend_bytes': 'server.quota.backend.bytes',
    'etcd_server_read_indexes_failed_total': 'server.read_indexes.failed.total',
    'etcd_server_slow_apply_total': 'server.apply.slow.total',
    'etcd_server_slow_read_indexes_total': 'server.read_indexes.slow.total',
    'etcd_snap_db_fsync_duration_seconds': 'snap.db.fsync.duration.seconds',
    'etcd_snap_db_save_total_duration_seconds': 'snap.db.save.total.duration.seconds',
    'etcd_snap_fsync_duration_seconds': 'snap.fsync.duration.seconds',
    'go_gc_duration_seconds': 'go.gc.duration.seconds',
    'go_goroutines': 'go.goroutines',
    'process_max_fds': 'process.max.fds',
    'process_open_fds': 'process.open.fds',
    'process_resident_memory_bytes': 'process.resident.memory.bytes',
    'process_virtual_memory_bytes': 'process.virtual.memory.bytes'
}
